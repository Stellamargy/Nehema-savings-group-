from .database_extensions import db
from sqlalchemy import Column , Integer ,String , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class SaccoMemberProfile(db.Model):
    __tablename__ = "sacco_member_profiles"
    id = Column(Integer, primary_key=True)
    # Foreign Key uniqueness enforces a one to one relationshi
    user_id = Column(Integer,ForeignKey("user.id"), unique=True, nullable=False)
    member_no = db.Column(db.String(50), unique=True, nullable=False)
    joining_date = db.Column(db.DateTime, default=datetime.utcnow)
    # savings_balance = db.Column(db.Float, default=0.0)

    #Define Relationships
    user=relationship('User', back_populates="sacco_member_profile",secondary="user",uselist=False)
