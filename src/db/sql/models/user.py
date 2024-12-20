from src.db.sql.models import SQL_Base
from sqlalchemy import Column, Integer, String, Boolean

class User(SQL_Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    role = Column(String(15), nullable=False)
    endorsements = Column(Integer, default=0)
    reports = Column(Integer, default=0)
    banned = Column(Boolean, default=False)


    def as_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__tablename__.columns}

