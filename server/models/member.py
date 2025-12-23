# from .database_extensions import db
from server.models.database_extensions import db
from sqlalchemy import Column , Integer ,String , ForeignKey,event
from sqlalchemy.orm import relationship
from datetime import datetime

class Member(db.Model):
    #table name
    __tablename__ = "members"
    #table columns and member instance attributes 
    id = Column(Integer, primary_key=True)
    # Foreign Key uniqueness enforces a one to one relationship
    user_id = Column(Integer,ForeignKey("users.id"), unique=True, nullable=False)
    member_no = db.Column(db.String(), unique=True, nullable=False)
    joining_date = db.Column(
        db.DateTime, 
        default=datetime.utcnow()
        )
    

    #Define Pythonic Relationships
    user=relationship('User', back_populates="member",uselist=False)
    ledger_accounts=relationship("LedgerAccount" , back_populates="member")


    
@event.listens_for(Member, "before_insert")
def generate_member_no(mapper, connection, target):
    last_number = connection.execute(
        db.text("SELECT member_no FROM members ORDER BY id DESC LIMIT 1")
    ).fetchone()

    if last_number is None:
        next_no = 1
    else:
        last_no_int = int(last_number[0].split("-")[1])
        next_no = last_no_int + 1

    target.member_no = f"MBR-{next_no:05d}"

