from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,func,DateTime,Integer

# Base Class for models
class Base(DeclarativeBase):
  created_at=Column (DateTime(timezone=True),server_default=func.now())
  updated_at=Column(DateTime(timezone=True),onupdate=func.now())