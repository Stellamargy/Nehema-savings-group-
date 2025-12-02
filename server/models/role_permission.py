from sqlalchemy import Table, Column ,Integer, ForeignKey
role_permissions=Table(
    "role_permissions",#table name manually , no class mapping
    #column name , column data type , constraints
    Column("role_id",Integer ,ForeignKey("roles.id"), primary_key=True),
    Column("permission_id",Integer ,ForeignKey("permissions.id"),primary_key=True)
)