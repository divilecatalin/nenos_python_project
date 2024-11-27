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

def update_user_in_db(user_id: int, dto: UserDto) -> bool:
    """
    Update a user in the database 
    """ 
    with SQLSession() as session:
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return False
        user.username = dto.username
        user.email = dto.email
        user.role = dto.role
        user.endorsements = dto.endorsements
        user.reports = dto.reports
        user.banned = dto.banned
        session.commit()
        return True

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