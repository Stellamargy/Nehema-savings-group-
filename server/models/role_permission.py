from .database_extensions import db
# from .role import Role
# from .permission import Permission
role_permissions=db.Table(
    "role_permissions",#table name manually , no class mapping
    #column name , column data type , constraints
    db.Column("role_id",db.Integer ,db.ForeignKey("role.id"), primary_key=True),
    db.Column("permission_id",db.Integer ,db.ForeignKey("permission.id"),primary_key=True)
)