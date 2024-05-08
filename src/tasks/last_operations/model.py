from database import Base
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String


class Last_operation(Base):
    __tablename__ = "last_operation"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    operation = Column(String)
    timestamp = Column(DateTime)
    status_ok = Column(Boolean)
