from server.services.base_user import BaseUser
from server.services.ledger_manager import LedgerManager
from server.models import Role, db, Member, User
from server.services.email_manager import EmailManager
from server.extensions import mail
from server.utils import ConflictError
import secrets, string
import logging

logger = logging.getLogger(__name__)

class MemberOnboarding:
    @staticmethod
    def is_member_unique(member_data):
        if not BaseUser.is_email_unique(member_data["email"]):
            raise ConflictError("Email already exist")
        if not BaseUser.is_phone_unique(member_data["phone"]):
            raise ConflictError("Phone already exist")
        if not BaseUser.is_id_number_unique(member_data["id_number"]):
            raise ConflictError("ID number already exist")
        return True
    
    @staticmethod
    def generate_temporary_passwd(length=15):
        alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    @staticmethod
    def create_member_profile(user_id):
        profile = Member(user_id=user_id)
        db.session.add(profile)
        db.session.flush()
        return profile

    @classmethod
    def onboard_member(cls, member_data):
        """
        Onboards a new member with proper error handling.
        
        Returns:
            tuple: (user, email_sent_successfully)
        """
        user = None
        temporary_password = None
        
        try:
            # Check if member is unique before onboarding
            cls.is_member_unique(member_data)
            
            # Create temporary password
            temporary_password = cls.generate_temporary_passwd()
            member_data["_password_hash"] = temporary_password
            
            # Create user instance
            user = BaseUser.create_user(member_data)
            
            # Create member profile for the user
            profile = cls.create_member_profile(user.id)
            
            # Assign member role to the user
            member_role = Role.query.filter_by(name="MEMBER").one_or_none()
            if member_role:
                user.roles.append(member_role)
                # Assign a member a primary account
                primary_account = LedgerManager.create_primary_acc(profile.id)
            
            # COMMIT FIRST - ensure user is saved before sending email
            db.session.commit()
            
        except Exception as e:
            # If anything fails during user creation, rollback
            db.session.rollback()
            logger.error(f"Failed to create user: {str(e)}")
            raise
        
        # Now try to send email AFTER successful commit
        email_sent = False
        try:
            onboarding_email = EmailManager.send_account_setup_email(
                user_email=user.email,
                first_name=user.first_name,
                temporary_password=temporary_password
            )
            mail.send(onboarding_email)
            email_sent = True
            
        except Exception as e:
            # Log the error but don't fail the entire operation
            logger.error(
                f"User {user.id} created successfully but email failed: {str(e)}"
            )
            # You could:
            # - Add user to a "pending email" queue for retry
            # - Set a flag on user model indicating email not sent
            # - Notify admin
            # - Store in a separate "failed emails" table
        
        return user, email_sent