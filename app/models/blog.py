from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text, func
from app.db.base import Base
from sqlalchemy.orm import relationship
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    tags = Column(String,nullable=True)  
    author = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default= func.now())
    updated_at = Column(DateTime(timezone=True), onupdate= func.now(),nullable=True)

    user_id = Column(Integer,ForeignKey('users.id'))
    creator = relationship("User",back_populates="blogs")



