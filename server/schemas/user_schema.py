from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..models import User,db
from marshmallow import fields,ValidationError,validate




class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=User
        load_instance=True
        #serialization
        include_relationships=True
        sqla_session=db.session

    #  __tablename__="users"
    # id = Column(Integer, primary_key=True)
    # first_name = Column(String(50), nullable=False)
    # last_name = Column(String(50), nullable=False)
    # email = Column(String(50), unique=True, nullable=False)
    # phone = Column(String(13), unique=True, nullable=False)
    # id_number=Column(Integer,unique=True,nullable=False)
    # password = Column(String(15), nullable=False)
    # active=Column(Boolean,nullable=False,default=False)
    #Validation 
    first_name=fields.String(required=True,validate=validate.Length(min=3,max=50))
    last_name=fields.String(required=True,validate=validate.Length(min=3,max=50))
    #unique
    email=fields.Email(required=True,validate=validate.Length(min=10,max=50))
    #unique and how does a real phone number look like
    phone=fields.String(required=True,validate=validate.Length(equal=13))
    #unique id number
    id_number=fields.String(required=True,validate=validate.Length(min=8,max=14))
    #how does a secure password look like ?
    password=fields.String(required=True,validate=validate.Length(min=6,max=15))
    active=fields.Boolean(required=True,load_default=False)

    #custom validation 
    #unique email 
    @validates("email")
    def unique_email(self,value):
        email=User.query.filter_by(email=value).first()
        if email:
            raise ValidationError("Email already exist")
    


