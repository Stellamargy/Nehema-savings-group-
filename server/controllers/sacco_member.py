from flask import Blueprint ,request ,jsonify
#Define the blueprint
sacco_member_bp=Blueprint("sacco_member_bp", __name__, url_prefix="/sacco_members")


# Route to add sacco_members
@sacco_member_bp.post("/create")
def create_sacco_member():
    pass

