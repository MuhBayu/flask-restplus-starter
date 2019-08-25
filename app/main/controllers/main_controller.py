from flask import request
from flask_restplus import Resource
from ..utils.dto import MainDto

api = MainDto.api

@api.route('/')
class IndexRoute(Resource):
    def get(self):
        return {"code": 200}, 200