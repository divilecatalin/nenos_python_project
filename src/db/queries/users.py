from src.common.data_transfer_objects.users import UserDto
from src.db.sql.models import User
from src.db.sql.connection import SQLSession

def add_user_in_db(username: str, email: str, role: str) -> None:
    """
    Add a user into the database 
    """ 
    with SQLSession() as session:
        user = User(
            username=username,
            email=email,
            role=role
        )
        session.add(user)
        session.commit()

def get_user_from_db(user_id: int) -> UserDto:
    """
    Retrieve a user from the database 
    """ 
    with SQLSession() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            return UserDto(
                username=user.username,
                email=user.email,
                role=user.role,
                endorsements=user.endorsements,
                reports=user.reports,
                banned=user.banned
            )
        return None

def update_user_in_db(user_id: int, dto: UserDto) -> UserDto:
    """
    Update a user in the database 
    """ 
    with SQLSession() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        user.username = dto.username or user.username
        user.email = dto.email or user.email
        user.role = dto.role or user.role
        user.endorsements = (user.endorsements or 0) + (dto.endorsements or 0)
        user.reports = (user.reports or 0) + (dto.reports or 0)
        user.banned = user.reports >=10
        session.commit()
        session.refresh(user)
        return UserDto(
                username=user.username,
                email=user.email,
                role=user.role,
                endorsements=user.endorsements,
                reports=user.reports,
                banned=user.banned
            )

def delete_user_from_db(user_id: int) -> bool:
    """
    Delete a user from the database 
    """ 
    with SQLSession() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        session.delete(user)
        session.commit()
        return True