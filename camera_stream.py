import logging
import os
import platform
import psutil
import time
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()

# --- Agent Identity Config ---
AGENT_PROFILE = {
    "agent_name": "Nucleus-Curiosity-v1",
    "purpose": "Autonomous Educational Incitement",
    "target_audience": "Rural Indian Students",
    "pipeline_backend": "tool_ai local inference",
    "birth_time": time.strftime("%Y-%m-%d %H:%M:%S")
}

@router.get("/system/stats")
async def get_stats():
    """
    Transforms the old system stats into a LIVE hardware monitor.
    The UI graphs will now map real CPU, RAM, and runtime metrics!
    """
    # Fetch real system metrics using psutil
    cpu = psutil.cpu_percent(interval=None)
    memory = psutil.virtual_memory().percent
    
    # Attempt to read actual thermal data safely across platforms
    temperature = 0.0
    if hasattr(psutil, "sensors_temperatures"):
        temps = psutil.sensors_temperatures()
        if temps:
            # Grab the first available core temperature sensor
            for name, entries in temps.items():
                if entries:
                    temperature = entries[0].current
                    break

    return {
        "time": time.strftime("%H:%M:%S"),
        "cpu_percent": cpu,
        "memory_percent": memory,
        "temperature": temperature
    }

@router.get("/video_feed")
async def video_feed():
    """
    Instead of an empty stream, this acts as an information dump explaining 
    the system environment layout.
    """
    return {
        "status": "System Identity Active",
        "environment": {
            "os": platform.system(),
            "os_release": platform.release(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "python_version": platform.python_version()
        }
    }

@router.get("/gallery/images")
async def list_gallery_images():
    """
    Maps the static gallery into an inspecting looking-glass for the Agent's core specs.
    """
    return {
        "status": "success",
        "agent_manifest": AGENT_PROFILE,
        "images": [
            {"id": "manifest_01", "title": f"Identity: {AGENT_PROFILE['agent_name']}"},
            {"id": "manifest_02", "title": f"Objective: {AGENT_PROFILE['purpose']}"}
        ]
    }

# --- Retain standard mocks for actions to keep buttons safe from throwing errors ---
@router.post("/camera/start")
async def start_camera():
    return {"status": "Telemetry logging engaged", "agent": AGENT_PROFILE["agent_name"]}

@router.post("/camera/stop")
async def stop_camera():
    return {"status": "telemetry_held"}

@router.post("/camera/capture")
async def capture_image():
    return {"status": "snapshot_disabled", "error": "Use system/stats for telemetry"}

@router.post("/camera/detection/start")
async def start_detection():
    return {"status": "agent_monitoring_active"}

@router.post("/camera/detection/stop")
async def stop_detection():
    return {"status": "agent_monitoring_paused"}