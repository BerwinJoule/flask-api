from collections import OrderedDict
from flask import request, jsonify, abort
from src.main import app
from src.models.user import User

import json

@app.route("/v1/statistics/<project_id>", methods = ['POST'])
def usage_statistics(project_id):
    if project_id:
        return json.dumps(OrderedDict([(project_id, "ok")]))
    else:
        abort(401)