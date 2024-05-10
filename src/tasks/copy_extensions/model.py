from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String


class Copy_Extensions(Base):
    __tablename__ = "copy_extensions"

    id = Column(Integer, primary_key=True)
    from_dirs_id = Column(Integer, ForeignKey("from_dirs.id"), nullable=False)
    extension = Column(String, nullable=False)
    min_size_file = Column(Integer, nullable=False)
    max_size_file = Column(Integer, nullable=False)
