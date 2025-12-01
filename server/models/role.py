from .database_extensions import db
from sqlalchemy import Column,Integer,String,Text
class Role(db.Model):
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    description=Column(Text)