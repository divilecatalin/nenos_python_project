from fastapi import APIRouter, Response , HTTPException

from src.common.data_transfer_objects.users import UserDto
from src.db.queries.users import add_user_in_db
from src.db.queries.users import get_user_from_db
from src.db.queries.users import update_user_in_db
from src.db.queries.users import delete_user_from_db

router = APIRouter()

@router.put("")
def add_user(dto: UserDto) -> Response:
    """ 
    Add a user to the database 
    """ 
    add_user_in_db(
        username=dto.username, 
        email=dto.email, 
        role=dto.role 
    )
    return Response(status_code=201)

@router.get("/{user_id}", response_model=UserDto)
def get_user(user_id: int) -> UserDto:
    """ 
    Retrieve a user from the database 
    """ 
    user = get_user_from_db(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User  not found")
    return user

@router.patch("/{user_id}",response_model=UserDto)
def update_user(user_id: int, dto: UserDto) -> Response:
    """ 
    Update an existing user in the database 
    """ 
    updated = update_user_in_db(user_id, dto)
    if not updated:
        raise HTTPException(status_code=404, detail="User  not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: int) -> Response:
    """ 
    Delete a user from the database 
    """ 
    deleted = delete_user_from_db(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User  not found")
    return Response(status_code=204)