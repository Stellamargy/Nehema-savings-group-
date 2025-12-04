from .database_extensions import db
from sqlalchemy import Column , Integer ,String,Boolean
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(120), nullable=False)
    last_name = Column(String(120), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50), unique=True, nullable=False)
    id_number=Column(Integer,unique=True,nullable=False)
    password = Column(String(255), nullable=False)
    active=Column(Boolean,nullable=False,default=True)

     #Define Relationships
    sacco_member_profile=relationship(
        'SaccoMemberProfile', 
        back_populates="user",
        secondary="sacco_member_profiles",
        uselist=False,
        cascade="all, delete-orphan"

        )
    

    administrator_profile = relationship(
        "AdministratorProfile", 
        back_populates="user",
        secondary="administrator_profiles",
        uselist=False,
        cascade="all, delete-orphan"
        )