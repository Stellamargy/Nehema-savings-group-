# from .database_extensions import db
from server.models.database_extensions import db
from sqlalchemy import Column,Integer,String,Text,Enum,CheckConstraint
from sqlalchemy.orm import relationship


class Role(db.Model):
    # Table name
    __tablename__="roles"
    #Table columns and role instance attributes
    id=Column(Integer,primary_key=True)
    name=Column(String,nullable=False,unique=True)
    description=Column(Text)

    __table_args__ = (
        CheckConstraint(
            "name IN ('admin', 'member')",
            name="check_role_name"
        ),
    )

    # define pythonic relationships
    permissions=relationship(
        "Permission",
        back_populates="roles",
        secondary="role_permissions",
        
        )
    users = relationship(
    "User",
    secondary="user_roles",
    back_populates="roles",
    )


