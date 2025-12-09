# from .database_extensions import db
from server.models.database_extensions import db
role_permissions=db.Table(
    "role_permissions",#table name manually , no class mapping
    #column name , column data type , constraints
    db.Column("role_id",db.Integer ,db.ForeignKey("roles.id"), primary_key=True),
    db.Column("permission_id",db.Integer ,db.ForeignKey("permissions.id"),primary_key=True)
)