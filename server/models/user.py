# from .database_extensions import db
from server.models.database_extensions import db
from sqlalchemy import Column , Integer ,String,Boolean
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__="users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    phone = Column(String(13), unique=True, nullable=False)
    id_number=Column(String(14),unique=True,nullable=False)
    password = Column(String(), nullable=False)
    active=Column(Boolean,nullable=False,default=False)

     #Define Relationships
    sacco_member_profile=relationship(
        'SaccoMemberProfile', 
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"

        )
    

    administrator_profile = relationship(
        "AdministratorProfile", 
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
        )

    roles = relationship(
    "Role",
    secondary="user_roles",
    back_populates="users",
    )

    
    def __str__(self):
        return (
        f"User({{"
        f"'id': {self.id}, "
        f"'first_name': '{self.first_name}', "
        f"'last_name': '{self.last_name}', "
        f"'email': '{self.email}', "
        f"'phone': '{self.phone}', "
        f"'id_number': '{self.id_number}', "
        f"'password': '{self.password}', "
        f"'active': {self.active}"
        f"}})"
    )
