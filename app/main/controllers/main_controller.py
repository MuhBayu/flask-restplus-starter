from flask import request
from flask_restplus import Resource

from ..utils.dto import MainDto
from ..utils.decorator import token_required

api = MainDto.api

@api.route('/')
class IndexRoute(Resource):
    @token_required
    def get(self):
        return {"status": 200}, 200