from src.db.sql.models import SQL_Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Product(SQL_Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    description = Column(String(100), default = "No description")
    price = Column(Float, nullable = False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable = False)
    tags = Column(String(20))


    def as_dict(self):
        return {col.name:getattr(self, col.name) for col in self.__tablename__.columns}
