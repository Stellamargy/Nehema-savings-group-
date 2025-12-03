from .database_extensions import db 
user_roles=db.Table(
    "user_roles",
    db.Column("user_id",db.Integer,db.ForeignKey("users.id"),primary_key=True),
    db.Column("role_id",db.Integer,db.ForeignKey("role.id"),primary_key=True),
)