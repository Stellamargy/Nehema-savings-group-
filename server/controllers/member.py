from flask import Blueprint, request, jsonify
from server.schemas import UserSchema
from marshmallow import ValidationError
from werkzeug.exceptions import BadRequest
from server.utils import ConflictError
from server.services import MemberOnboarding
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
import logging

logger = logging.getLogger(__name__)

# Define the blueprint
member_bp = Blueprint(
    "member_bp",
    __name__,
)


# Route to add sacco_members
@member_bp.post("/member")
def add_member():
    try:
        member_request_data = request.json
        
        # Validate member request data using user schema
        user_schema = UserSchema()
        member_obj = user_schema.load(member_request_data)
        
        # Use member onboarding service to onboard (create a member)
        member, email_sent = MemberOnboarding.onboard_member(member_obj)
        
        # Serializing response data by using schema to be used as response
        response_data = user_schema.dump(member)
        
        # Return different messages based on email status
        if email_sent:
            return jsonify({
                "status": "success",
                "data": response_data,
                "message": "Member successfully created and welcome email sent"
            }), 201
        else:
            return jsonify({
                "status": "partial_success",
                "data": response_data,
                "message": "Member successfully created, but welcome email could not be sent. Please contact support for login credentials.",
                "warning": "Email delivery failed"
            }), 201

    except BadRequest:
        return jsonify({
            "status": "error",
            "message": "Invalid JSON format"
        }), 400

    except ValidationError as error:
        return jsonify({
            "status": "error",
            "message": "Invalid data provided",
            "errors": error.messages
        }), 422

    except ConflictError as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 409

    except IntegrityError as error:
        logger.error(f"Database integrity error: {str(error)}")
        return jsonify({
            "status": "error",
            "message": "Database constraint violation. This may indicate duplicate data or invalid references.",
            "details": "Please check that all required fields are unique and valid"
        }), 409

    except SQLAlchemyError as error:
        logger.error(f"Database error during member creation: {str(error)}")
        return jsonify({
            "status": "error",
            "message": "Database error occurred while creating member",
            "details": "Please try again. If the problem persists, contact support."
        }), 500

    except Exception as error:
        logger.error(f"Unexpected error during member onboarding: {str(error)}", exc_info=True)
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred while creating member",
            "details": "Please contact support if this issue persists"
        }), 500
    



   
 


