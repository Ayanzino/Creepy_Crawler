"""Settings routes."""

from flask import Blueprint, request
from flask_migrate import Migrate
from app.models import db, User, Theme
from flask_login import current_user, login_required
from app.s3_helpers import (upload_file_to_s3, allowed_file, get_unique_filename)

settings_routes = Blueprint('settings', __name__)

def validation_errors_to_error_messages(validation_errors):
    """Turn the WTForms validation errors into a simple list."""
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

@settings_routes.route('/media', methods=['PATCH'])
@login_required
def upload_media():
    """Upload media to aws and update database."""
    if 'media' not in request.files:
        return {'errors': 'media required'}, 400

    media = request.files['media']

    media.filename = get_unique_filename(media.filename)

    upload = upload_file_to_s3(media)

    #? if dict has no filename key
    if 'url' not in upload:
        return upload, 400

    url = upload['url']
    edited_user = User(
        id=current_user.id,
        media=url
    )
    db.session.add(edited_user)
    db.seesion.commit()
    return {'url': url}

@settings_routes.route('/', methods=['POST'])
def add_theme():
    """Add a theme."""
    theme_data = request.json
    print(theme_data)

    theme = Theme()
    theme_data.populate_obj(theme)
    db.session.add(theme)
    db.session.commit()

# * Add the line below after each conditional
# * return {'errors': validation_errors_to_error_messages(form.errors)}, 400
