from fastapi import APIRouter

router = APIRouter()


@router.get("/api/status")
def status():

    return {
        "status": "online",
        "version": "0.1.0"
    }