from app import ma
from .model import User


class UserSchema(ma.Schema):
    class Meta:
        model=User
        fields = ('id','username', 'email')


class JokeSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'body')


"""for future reference"""
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
# This part defined structure of response of our endpoint. We want that all of our endpoint will have JSON response. Here we define that our JSON response will have two keys(username, and email). Also we defined user_schema as instance of UserSchema, and user_schemas as instances of list of UserSchema.
