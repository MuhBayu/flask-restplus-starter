from flask_restplus import Namespace, fields


class MainDto:
    api = Namespace('/', description='testing')