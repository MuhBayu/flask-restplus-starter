from functools import wraps
from flask import request

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "x-access-token" in request.headers:
            token = request.headers['x-access-token']
            return f(*args, **kwargs)
        else:
            return {"code": 401, "message": "Token required"}, 401

    return decorated