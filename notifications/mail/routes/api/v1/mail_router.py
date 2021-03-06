
from flask import request, jsonify
from flask_cors import CORS, cross_origin

from . import endpoints
from notifications.mail.services import send
from notifications.mail.serializers import sendmail
from notifications.helpers import error

@endpoints.route('/mail/send', strict_slashes=False, methods=['POST'])
@cross_origin()
def send_mail_endpoint():
    if not request.get_json():
        return error(status=400, error_message="Empty payload")

    response = send.execute(request.get_json())
    if 'error_message' in response:
        return error(status=response['status'], error_message=response['error_message'])

    data = sendmail.serialize(message=response['message'])
    return jsonify(data), 200
