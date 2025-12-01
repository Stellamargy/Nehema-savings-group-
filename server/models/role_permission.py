from sqlalchemy import Table, Column ,Integer
role_permission=Table(
    "roles_permissions",
    Column("role_id",Integer ,primary_key=True),
    Column("permission_id",Integer ,primary_key=True)
)