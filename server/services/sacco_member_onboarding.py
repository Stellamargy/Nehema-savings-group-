from server.services import BaseUser
from server.models import SaccoMemberProfile,Role,db
class SaccoMemberOnboarding():
    @staticmethod
    def create_saccomember_profile(id):
        profile=SaccoMemberProfile(user_id=id)
        return profile



    @classmethod
    def create_sacco_member (cls,member_data):
        
        # Get user id
        user=BaseUser.create_user(member_data)
        user_id=user.id
        #sacco member profile
        profile=cls.create_saccomember_profile(user_id)

        #assign sacco member role 
        sacco_member_role=Role.query.filter_by(name="Sacco-Member").one_or_none()
        if role:
            user.roles.append[sacco_member_role]
        

        #add to the database 
        db.session.add(profile)
        #commit the changes 
        db.session.commit ()
        return user 

        
        