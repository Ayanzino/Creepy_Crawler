from flask import Blueprint, request
from flask_migrate import Migrate
from app.models import db

settings_routes = Blueprint('settings', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

# * Add the line below after each conditional
# * return {'errors': validation_errors_to_error_messages(form.errors)}, 401
