from .database_extensions import db
from sqlalchemy import Column,Integer,String,Text,ForeignKey
from sqlalchemy.orm import relationship

class AdministratorProfile(db.Model):
    __tablename__="administrator_profiles"

    id = Column(Integer, primary_key=True)
    #Foreign Key uniqueness enforces a one to one relationship
    user_id = Column(db.Integer, ForeignKey("users.id"), unique=True, nullable=False)
    staff_number = db.Column(db.String(50), unique=True, nullable=False)
    #relationship 
    user = relationship("User", back_populates="administrator_profile",secondary="users",uselist=False)
    