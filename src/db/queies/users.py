from src.db.sql.models import User
from src.db.sql.connection import SQLSession

def add_user_in_db(username : str,email : str,role : str) -> None:
    """
    Add an user into the database
    """
    with SQLSession() as session:
        user = User(
            username = username,
            email = email,
            role = role,
        )
        session.add(user)
        session.commit()