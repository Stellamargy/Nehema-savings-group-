from sqlalchemy import Column,Integer,String,Text
from .database_extensions import db
from sqlalchemy.orm import relationship
class Permission(db.Model):
    id=Column(Integer,primary_key=True)
    code=Column(String,nullable=False)
    description=Column(Text,nullable=False)

    #pythonic relationship
    roles=relationship("Role",back_populates="permissions",secondary="role_permissions")