from server.services.base_user import BaseUser
from server.services.ledger_management import LedgerManagement
from server.models import SaccoMemberProfile,Role,db
from server.services.email_manager import EmailManager
from server.extensions import mail

class SaccoMemberOnboarding():
    @staticmethod
    def create_saccomember_profile(id):
        profile=SaccoMemberProfile(user_id=id)
        db.session.add(profile)
        db.session.flush()
        return profile

    @classmethod
    def create_sacco_member (cls,member_data):
        
        # Get user id
        user=BaseUser.create_user(member_data)
        user_id=user.id
        #sacco member profile
        profile=cls.create_saccomember_profile(user_id)

        #assign sacco member role 
        sacco_member_role=Role.query.filter_by(name="MEMBER").one_or_none()
        if sacco_member_role:
            user.roles.append(sacco_member_role)
        #Assign a member a primary account at creation 
        primary_account=LedgerManagement.create_primary_acc(profile.id)

        #Send onboarding email
        onboarding_email=EmailManager.send_account_setup_email(
            user_email=user.email,
            first_name=user.first_name,
            temporary_password=user.password
        )
        #Send email
        mail.send(onboarding_email)
        
        #commit the changes 
        db.session.commit ()


        
        return user 

        
        