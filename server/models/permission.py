from sqlalchemy import Column,Integer,String,Text
from .database_extensions import db
class Permission(db.Model):
    id=Column(Integer,primary_key=True)
    code=Column(String,nullable=False)
    description=Column(Text,nullable=False)