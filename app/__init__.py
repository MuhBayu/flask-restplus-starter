from flask_restplus import Api
from flask import Blueprint

from .main.controllers.main_controller import api as main_controller

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
)

api.add_namespace(main_controller, path='/')