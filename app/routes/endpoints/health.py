import psutil
from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix="/health",
    tags=["health"],
)

@router.get("", tags=["health"])
async def health_check():
    try:
        # Get system metrics
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status": "healthy",
                "system_info": {
                    "cpu_usage": f"{cpu_usage}%",
                    "memory_usage": f"{memory_usage}%",
                    "disk_usage": f"{disk_usage}%"
                }
            }
        )
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "unhealthy",
                "error": str(e)
            }
        )
