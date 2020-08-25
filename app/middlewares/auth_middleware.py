from functools import wraps
from flask import request, abort, Response, jsonify

from app.utils import validate_token

def is_auth(f):
    @wraps(f)
    def _is_auth(*args, **kwargs):
        authorization = request.headers.get('Authorization')
        token_validation = validate_token(authorization)
        if token_validation[0]:
            return f(*args, **kwargs, token_payload=token_validation[1])
        else:
            abort(403, token_validation[1])
    return _is_auth
