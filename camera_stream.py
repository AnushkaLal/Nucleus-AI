import logging
from fastapi import APIRouter

logger = logging.getLogger(__name__)
router = APIRouter()

# --- Mock Camera Endpoints to Prevent Frontend/Backend Network Crashes ---

@router.get("/system/stats")
async def get_stats():
    # Return basic dummy stats so the UI graphs don't break
    import time
    return {
        "time": time.strftime("%H:%M:%S"),
        "cpu_percent": 0.0,
        "memory_percent": 0.0,
        "temperature": 0.0
    }

@router.post("/camera/start")
async def start_camera():
    return {"status": "disabled_for_nucleus_edu"}

@router.post("/camera/stop")
async def stop_camera():
    return {"status": "stopped"}

@router.get("/video_feed")
async def video_feed():
    return {"status": "Camera feed uninstalled"}

@router.post("/camera/capture")
async def capture_image():
    return {"status": "disabled"}

@router.post("/camera/detection/start")
async def start_detection():
    return {"status": "disabled"}

@router.post("/camera/detection/stop")
async def stop_detection():
    return {"status": "stopped"}

@router.get("/gallery/images")
async def list_gallery_images():
    return {"status": "success", "images": []}
