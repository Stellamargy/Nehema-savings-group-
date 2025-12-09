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
    admin, _ = get_or_create(Role, name="Administrator")
    sacco_member, _ = get_or_create(Role, name="Sacco-Member")

    # --- Permissions ---
    create_member_perm, _ = get_or_create(
        Permission,
        code="CREATE_SACCO_MEMBER",
        description="Add Sacco Members to the System"
    )

    # --- Associations ---
    if create_member_perm not in admin.permissions:
        admin.permissions.append(create_member_perm)

    db.session.commit()
    print("Seeding complete!")



with app.app_context():
    seed()

