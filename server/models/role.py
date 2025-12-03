from .database_extensions import db
from sqlalchemy import Column,Integer,String,Text
from sqlalchemy.orm import relationship

class Role(db.Model):
    
    #data type , constraints
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    description=Column(Text)

    # define pythonic relationships
    #name of the model , back_populates ,
    permissions=relationship("Permission",back_populates="roles",secondary="role_permissions")

