from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class To_dir(Base):
    __tablename__ = "to_dir"

    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    path_to_dir = Column(String, nullable=False)
    create_dir_day = Column(Boolean, default=False)
    create_dir_hour = Column(Boolean, default=False)
    create_dir_extension = Column(Boolean, default=False)
