import json

from flask import Blueprint
from flask import Response

error_handler = Blueprint('error_handler', import_name=__name__)


@error_handler.errorhandler(404)
def page_not_found(e):
    return Response(
        json.dumps({
            'status': False,
            'message': "page not found",
        }),
        mimetype='application/json'
    ), 404


@error_handler.errorhandler(500)
def internal_server_error(e):
    return Response(
        json.dumps({
            'status': False,
            'message': "internal server error",
        }),
        mimetype='application/json'
    ), 500


@error_handler.errorhandler(429)
def too_many_requests_error(e):
    return Response(
        json.dumps({
            'status': False,
            'message': "Sorry, you are making too many requests to our servers",
        }),
        mimetype='application/json'
    ), 429
