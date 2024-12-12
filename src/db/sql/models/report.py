from src.db.sql.models import SQL_Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Report(SQL_Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key = True)
    reported_user = Column(Integer, ForeignKey("users.id"), nullable = False)
    reason = Column(String(50), nullable = False)
    reporter_id = Column(Integer, ForeignKey("users.id"), nullable = False)

    def as_dict(self):
        return {col.name:getattr(self, col.name) for col in self.__tablename__.columns}
