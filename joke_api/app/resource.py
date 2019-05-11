from flask_restful import Resource, reqparse
from flask import request, json
from .model import User
from .schema import UserSchema
from app import api, db
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash


class UserApiPk(Resource):

    def get(self, pk):
        user = User.query.get_or_404(pk, description="user with this id doens't exit")

        user_schema = UserSchema()
        result = user_schema.dump(user)
        return {'user': result}

    """post for signup the user"""

    def post(self):
        print(request.data)
        json_input = request.get_json()
        print('got post')
        if not json_input:
            return {'error ': 'bad request'}, 400

        # handler for UserSchema
        user_schema = UserSchema()

        # first check the format of the request
        try:
            data = user_schema.load(json_input)
            print('data', data)

            """the below line fixed the issue with validation error"""
            # pip install - U marshmallow - -pre

        except ValidationError as err:
            return {'errors': err.messages}, 422

        if User.query.filter_by(username=data['username']).first():
            return {'error': 'username exists'}, 400

        if User.query.filter_by(email=data['email']).first():
            return {'error': 'email exists'}, 400

        hashed_password = generate_password_hash(data['password'])

        new_user = User(data['username'], data['email'], hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return {"message": "new user added"}, 200

    # the see if the username and email already exists


class UserApiUsername(Resource):

    def get(self, username):
        print("username got the request")
        user = User.query.filter_by(username=username).first_or_404(description="user with this name doesn't exist")

        user_schema = UserSchema()
        result = user_schema.dump(user)
        print(result)
        return {'user': result}


api.add_resource(UserApiPk, '/joke/api/user/<int:pk>', endpoint='user')
api.add_resource(UserApiPk, '/joke/api/user/signup/', endpoint='signup')
api.add_resource(UserApiUsername, '/joke/api/user/<string:username>', endpoint='username')
