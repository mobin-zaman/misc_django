from flask_restful import Resource, reqparse
from flask import jsonify
from .model import User
from .schema import UserSchema
from app import api


class UserApi(Resource):

    def __init__(self):
        """the request parse for validating the arguments"""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required=True, help='No username provide', location='json')
        self.reqparse.add_argument('password',type=str,required=True,help='no password provided',location='json')
        self.reqparse.add_argument('email',type=str,required=True,help='no email provided',location='json')
        super(UserApi, self).__init__()

    def get(self, id):
        user = User.query.get(id)
        user_schema = UserSchema()
        output = user_schema.dump(user).data
        return {'user': output}

    def post(self,username,email,password):
        args=self.reqparse.parse_args()



api.add_resource(UserApi, '/joke/api/user/<int:id>', endpoint='user')
