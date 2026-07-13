"""
Nucleus AI Curiosity Scheduler: Sparks learning at scheduled intervals.
- Interval: Every N hours/days -> injects a dynamic curiosity prompt to the local model.
- Schedule: Runs at a specific time once -> triggers an educational challenge.
"""
import json
import logging
import os
import time
import uuid
import random
from typing import Any, Callable, Dict, List, Optional

from config import JOBS_FILE

logger = logging.getLogger(__name__)
_scheduler = None
_conv_manager = None


def _load_jobs() -> List[dict]:
    if not os.path.exists(JOBS_FILE):
        return []
    with open(JOBS_FILE, "r") as f:
        return json.load(f)


def _save_jobs(jobs: List[dict]) -> None:
    with open(JOBS_FILE, "w") as f:
        json.dump(jobs, f, indent=2)


def _get_prompt_from_payload(payload: dict) -> str:
    if not payload:
        return ""
    base_prompt = (payload.get("message") or payload.get("text") or "").strip()
    
    # TWEAK: Specialized curiosity injection for rural Indian students
    if not base_prompt:
        rural_themes = [
            # Organic Farming & Nature Science
            "Create a short, inspiring story about earthworms ('the farmer's best friends') and how they make soil healthy through organic farming. Keep it simple and ask a fun question about mud at the end.",
            "Explain how plants 'drink' water from the ground and breathe sunlight, comparing a leaf to a tiny kitchen cooking food for the tree. End with a thoughtful question.",
            
            # Outer Space Exploration
            "Explain what stars are to a child who sleeps under the open sky. Describe the moon as a neighbor in space and mention how India sent Mangalyaan/Chandrayaan to explore other worlds. End with a question about flying.",
            "Describe the solar system like a massive village fair where the Sun sits in the center and all the planets, including Earth, walk around it in perfect circles. End with an inspiring question about what lies beyond.",
            
            # Inspirational Pioneers
            "Tell a 3-sentence inspiring story about Dr. APJ Abdul Kalam, the 'Missile Man of India', who grew up in a small coastal village and went on to build rockets and become President. Ask a question to inspire big dreams.",
            "Tell a quick, exciting story about how normal village seeds grow into giant banyan trees that live for hundreds of years, explaining the magic hidden inside a tiny seed."
        ]
        return random.choice(rural_themes)
        
    return base_prompt


def _is_recurring(schedule: Any) -> bool:
    if isinstance(schedule, dict):
        return schedule.get("kind") == "every"
    return False


def _run_job(job_id: str) -> None:
    """Called by scheduler when a curiosity trigger is due."""
    global _conv_manager
    jobs = _load_jobs()
    job = next((j for j in jobs if j.get("id") == job_id), None)
    if not job or not _conv_manager:
        return
        
    prompt = _get_prompt_from_payload(job.get("payload") or {})
    
    try:
        import tool_ai
        # Run through your local model pipeline
        tool_call_raw, tool_result = tool_ai.run_task_for_backend(prompt)
    except Exception as e:
        logger.warning("[curiosity_scheduler] tool_ai failed for job %s: %s", job_id, e)
        return
        
    # Label the incoming prompt as a systemic curiosity nudge
    user_msg = {"role": "user", "content": "✨ Curiosity Engine Prompt: " + prompt}
    
    result_text = str(tool_result) if tool_result is not None else "No spark generated."
    assistant_msgs = []
    if tool_call_raw:
        assistant_msgs.append({"role": "assistant", "content": tool_call_raw, "hidden": True})
    assistant_msgs.append({"role": "assistant", "content": result_text})
    
    conv_id = job.get("conversation_id")
    if conv_id:
        conv = _conv_manager.get_conversation(conv_id)
        if conv:
            conv["messages"].append(user_msg)
            conv["messages"].extend(assistant_msgs)
            _conv_manager.update_conversation(conv_id, conv["messages"])
            logger.info("[curiosity_scheduler] Appended new query spark to conversation %s", conv_id)
        else:
            # Recreate with a localized theme header
            conv = _conv_manager.create_conversation(title=job.get("name", "Daily Spark"), messages=[user_msg] + assistant_msgs)
            job["conversation_id"] = conv["id"]
            for i, j in enumerate(jobs):
                if j.get("id") == job_id:
                    jobs[i] = job
                    break
            _save_jobs(jobs)
    else:
        # Keep the UI clean for the hackathon presentation boards
        title = (job.get("name") or "Daily Riddle").strip()
        conv = _conv_manager.create_conversation(title=title, messages=[user_msg] + assistant_msgs)
        if _is_recurring(job.get("schedule")):
            job["conversation_id"] = conv["id"]
            for i, j in enumerate(jobs):
                if j.get("id") == job_id:
                    jobs[i] = job
                    break
            _save_jobs(jobs)
        logger.info("[curiosity_scheduler] Initiated curiosity tracking node: %s", conv['id'])


def init_scheduler(conv_manager) -> "APScheduler":
    """Initialize and return the background engine scheduler."""
    global _scheduler, _conv_manager
    try:
        from apscheduler.schedulers.background import BackgroundScheduler
    except ImportError:
        raise ImportError("Install APScheduler: pip install apscheduler")
    _conv_manager = conv_manager
    _scheduler = BackgroundScheduler()
    jobs = _load_jobs()
    for job in jobs:
        _schedule_one(job)
    _scheduler.start()
    logger.info("[curiosity_scheduler] Background learning triggers active.")
    return _scheduler


def _schedule_one(job: dict) -> bool:
    """Add one educational event window to the runner thread."""
    try:
        from apscheduler.triggers.interval import IntervalTrigger
        from apscheduler.triggers.date import DateTrigger
    except ImportError:
        return False
    job_id = job.get("id")
    if not job_id:
        return False
    schedule = job.get("schedule")
    if not schedule or not isinstance(schedule, dict):
        return False
    try:
        _scheduler.remove_job(job_id)
    except Exception:
        pass
    kind = schedule.get("kind")
    if kind == "every":
        every_ms = schedule.get("everyMs", 60000)
        seconds = max(1, every_ms // 1000)
        _scheduler.add_job(_run_job, IntervalTrigger(seconds=seconds), id=job_id, args=[job_id], replace_existing=True)
        return True
    if kind == "at":
        at_ms = schedule.get("atMs")
        if at_ms is None:
            return False
        from datetime import datetime
        run_date = datetime.fromtimestamp(at_ms / 1000.0)
        _scheduler.add_job(_run_job, DateTrigger(run_date=run_date), id=job_id, args=[job_id], replace_existing=True)
        return True
    return False


def list_jobs() -> List[dict]:
    return _load_jobs()


def add_job(name: str, description: str, schedule: Any, payload: dict) -> dict:
    job_id = str(uuid.uuid4())
    job = {
        "id": job_id,
        "name": name,
        "description": description or "",
        "schedule": schedule,
        "payload": payload or {},
        "conversation_id": None,
    }
    jobs = _load_jobs()
    jobs.append(job)
    _save_jobs(jobs)
    if _scheduler:
        _schedule_one(job)
    return job


def update_job(job_id: str, name: Optional[str] = None, description: Optional[str] = None, schedule: Any = None, payload: Optional[dict] = None) -> Optional[dict]:
    jobs = _load_jobs()
    job = next((j for j in jobs if j.get("id") == job_id), None)
    if not job:
        return None
    if name is not None:
        job["name"] = name
    if description is not None:
        job["description"] = description
    if schedule is not None:
        job["schedule"] = schedule
    if payload is not None:
        job["payload"] = payload
    _save_jobs(jobs)
    if _scheduler:
        _schedule_one(job)
    return job


def remove_job(job_id: str) -> bool:
    jobs = [j for j in _load_jobs() if j.get("id") != job_id]
    _save_jobs(jobs)
    if _scheduler:
        try:
            _scheduler.remove_job(job_id)
        except Exception:
            pass
    return True
