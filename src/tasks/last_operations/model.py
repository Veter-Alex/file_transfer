from database import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Last_operations(Base):
    __tablename__ = "last_operations"
    id = Column(Integer, primary_key=True)
    tasks_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    operation = Column(String)
    timestamp = Column(DateTime)
    status_ok = Column(Boolean)
