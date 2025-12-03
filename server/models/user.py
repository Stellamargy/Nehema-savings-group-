from .database_extensions import db
from sqlalchemy import Column , Integer ,String
from sqlalchemy.orm import relationship

class User(db.Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=False)
    id_number=Column(Integer(15),unique=True,nullable=False)
    password = Column(String(255), nullable=False)