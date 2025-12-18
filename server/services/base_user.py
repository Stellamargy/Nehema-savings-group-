from server.models import User ,db
from server.utils import ConflictError
class BaseUser():
    
    # uniqueness
    #check if email is unique
    @staticmethod
    def is_email_unique(email_address):
        existing_user_with_email=User.query.filter_by(email=email_address).first()
        if existing_user_with_email:
            return False
        else:
            return True
    # uniqueness
    #check if phone number is unique
    @staticmethod
    def is_phone_unique(phone_number):
        existing_user_with_phone=User.query.filter_by(phone=phone_number).first()
        if  existing_user_with_phone:
            return False
        else:
            return True
    # uniqueness
    #check if id number is unique
    @staticmethod
    def is_id_number_unique(id_no):
        existing_user_with_id_no=User.query.filter_by(id_number=id_no).first()
        if  existing_user_with_id_no:
            return False
        else:
            return True
    
    @classmethod
    def create_user(cls,data):
        #Business rule - a user can only have one account .
        #Check if a user is unique before creating one 
        #email
        if not cls.is_email_unique(data["email"]):
            raise ConflictError("Email already exist")
        #phone number
        if not cls.is_phone_unique(data["phone"]):
            raise ConflictError("Phone number already exist")
        # id number 
        if not cls.is_id_number_unique(data["id_number"]):
            raise ConflictError("ID number already exist")
        #create user
        user=User(**data)
        db.session.add(user)
        db.session.flush() # do not commit first - get the id of user 
        return user 

        