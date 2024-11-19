from src.db.sql.models import SQL_Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Transaction(SQL_Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    buyer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    seller_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    status = Column(String(15), default="PENDING")
    buyer_proof = Column(String(50), nullable=True)
    seller_proof = Column(String(50), nullable=True)
    buyer = relationship("User",foreign_keys=[buyer_id])
    seller = relationship("User", foreign_keys=[seller_id])
    product = relationship("Product", back_populates="transactions")

    def as_dict(self):
        return {col.name:getattr(self, col.name) for col in self.__tablename__.columns}