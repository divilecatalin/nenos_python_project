from fastapi import APIRouter, Response

from src.common.data_transfer_objects.users import UserDto
from src.db.queies.users import add_user_in_db

router = APIRouter()

@router.put("")
def add_user(dto: UserDto ) -> Response:
    """
    Add an user to the db
    """
    add_user_in_db(
        username = dto.username,
        email = dto.email,
        role = dto.role,
    )