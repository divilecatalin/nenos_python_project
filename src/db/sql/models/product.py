from src.db.sql.models import SQL_Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class Product(SQL_Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(100), default="No description")
    price = Column(Float, nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    tags = Column(String(20))

    #relations
    seller = relationship("User", back_populates="products")
    transactions = relationship("Transaction", back_populates="products")

    def as_dict(self):
        return {col.name:getattr(self, col.name) for col in self.__tablename__.columns}