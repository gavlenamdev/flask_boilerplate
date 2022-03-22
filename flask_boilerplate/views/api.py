import json
import logging

from flask import Response, Blueprint

api = Blueprint("api", import_name=__name__)
logger = logging.getLogger(__name__)


@api.route("/test")
def test():
    return Response(json.dumps({"message": "success"}), status=200, mimetype='application/json')
