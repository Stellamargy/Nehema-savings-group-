from flask import Blueprint ,request ,jsonify
from server.schemas import UserSchema
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from server.utils import ConflictError
from server.services import SaccoMemberOnboarding
#Define the blueprint
sacco_member_bp=Blueprint(
    "sacco_member_bp",
     __name__, 
    
     )


# Route to add sacco_members
@sacco_member_bp.post("/sacco-member")
def add_sacco_member():
    try:
        #python object
        sacco_member_data=request.json
         #Validate data
        user_schema=UserSchema()
        user_obj=user_schema.load(sacco_member_data)
        #Go to the sacco member service .
        sacco_member_user=SaccoMemberOnboarding.create_sacco_member(user_obj)

        serialized_user = user_schema.dump(sacco_member_user)

    except BadRequest:
         return jsonify({"error": "Invalid JSON"}), 400

    except ValidationError as error:
        
        return jsonify({
            "status":"Failed",
            "message":"Invalid data",
            "error":error.messages
        }),422
    except ConflictError as error:
        return jsonify({
            "status":"error",
            "message":str(error)
        }),409


    return jsonify({
        "data":serialized_user,
        "message":"User Succesfully created"
    }),201
    



   
 


