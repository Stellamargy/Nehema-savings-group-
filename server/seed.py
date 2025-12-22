#Seed data for testing 
# from .app import app
from server.app import app
from server.models import db ,Role,Permission,role_permissions
def get_or_create(model, **kwargs):
    instance = model.query.filter_by(**kwargs).first()
    if instance:
        return instance, False
    else:
        instance = model(**kwargs)
        db.session.add(instance)
        return instance, True
    
def seed():
    # --- Roles ---
    admin, _ = get_or_create(Role, name="ADMIN")
    sacco_member, _ = get_or_create(Role, name="MEMBER")

    # --- Permissions ---
    create_member_perm, _ = get_or_create(
        Permission,
        code="CREATE_MEMBER",
        description="Add Sacco Members to the System"
    )

    # --- Associations ---
    if create_member_perm not in admin.permissions:
        admin.permissions.append(create_member_perm)

    db.session.commit()
    print("Seeding complete!")

from sqlalchemy import text

def reset_data():
    db.session.execute(text("""
        TRUNCATE TABLE
            roles, 
            permissions,
            role_permissions,             
            users,
            sacco_member_profiles,
            administrator_profiles,
            user_roles,
            ledger_accounts
            
        RESTART IDENTITY CASCADE;
    """))
    db.session.commit()
    print("Resetting complete")


with app.app_context():
    seed()
    # reset_data()

