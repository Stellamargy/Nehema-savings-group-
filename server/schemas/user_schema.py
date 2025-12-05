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


    #Validation 
    first_name=fields.String(required=True,validate=validate.Length(min=3,max=50))
    last_name=fields.String(required=True,validate=validate.Length(min=3,max=50))
    email=fields.Email(required=True,validate=validate.Length(min=10,max=50))
    phone=fields.String(required=True,validate=validate.Length(equal=13))
    id_number=fields.Integer(required=True,validate=validate.Length(min=8,max=14))
    password=fields.String(required=True,validate=validate.Length(min=6))
    active=fields.Boolean(required=True,load_default=False)

    

