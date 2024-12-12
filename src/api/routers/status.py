from fastapi import APIRouter

from src.config import DB_NAME
from src.common.data_transfer_objects.api_status import APIStatusDto

router = APIRouter()

@router.get("/status")
def get_api_status() -> APIStatusDto:
    """
    Return API status along with database that is used within the API
    """
    return APIStatusDto(
        running=True,
        db_name=DB_NAME
    )
