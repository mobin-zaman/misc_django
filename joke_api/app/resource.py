from flask_restful import Resource, reqparse
from flask import request
from .model import User
from .schema import UserSchema
from app import api


class UserApi(Resource):

    def get(self, id):
        user = User.query.get_or_404(id,description="user doens't exit")

        user_schema = UserSchema()
        result = user_schema.dump(user).data
        return {'user': result}

    def post(self, username, email, password):
        json_request = request.json


api.add_resource(UserApi, '/joke/api/user/<int:id>', endpoint='user')
