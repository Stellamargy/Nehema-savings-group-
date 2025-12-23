from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from server.models import User,db
from marshmallow import fields, ValidationError, validate, validates
import re

#Schema is used for shape and format 
class UserSchema(SQLAlchemyAutoSchema):

    class Meta:
        model = User
        # load_instance = True
        # include_relationships = True
        sqla_session = db.session

    # Field validation
    first_name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    last_name = fields.String(required=True, validate=validate.Length(min=2, max=50))
    email = fields.Email(required=True, validate=validate.Length(min=10, max=50))
    phone = fields.String(required=True)
    id_number = fields.String(required=True, validate=validate.Length(min=8, max=14))
    #Since Autoschema validates field presence , I will overide it - password is not required
    #Password creation is a backend responsibility during user creation 
    _password_hash = fields.String(required=False)
    active = fields.Boolean(load_default="inactive")

    # Precompiled regex patterns
    PHONE_REGEX = re.compile(r'^(?:\+?254|0)(7\d{8}|1\d{8})$')
    

    @staticmethod 
    def is_phone_valid(number):
        return bool(UserSchema.PHONE_REGEX.match(number))

    #I will use this at changing password feature .

    # PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\W_]).{6,15}$')
    # @staticmethod
    # def is_password_strong(password):
    #     return bool(UserSchema.PASSWORD_REGEX.match(password))

    # @validates("password")
    # def validate_password(self, value,**kwargs):
    #     if not self.is_password_strong(value):
    #         raise ValidationError(
    #             "Password must be 6–15 characters and include at least one uppercase letter, "
    #             "one lowercase letter, one digit, and one special character."
    #         )

   
    @validates("phone")
    def validate_phone(self, value,**kwargs):
        # Uniqueness
        # existing = User.query.filter_by(phone=value).first()
        # if existing:
        #     raise ValidationError("Phone number already exists")

        # Format
        if not self.is_phone_valid(value):
            raise ValidationError("Phone number should be a valid Kenyan phone number")

    # @validates("id_number")
    # def unique_id_number(self, value,**kwargs):
    #     existing = User.query.filter_by(id_number=value).first()
    #     if existing:
    #         raise ValidationError("ID number already exists")

  


 
    

