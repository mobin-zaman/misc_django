from .model import User
from marshmallow import Schema, fields, validate, pre_load

"""custom validators"""

"""schemas for validation"""


class UserSchema(Schema):
    """below lines are for validating json request from post"""
    id = fields.Int(dump_only=True)
    username = fields.Str(80, required=True, validate=[validate.Length(min=5, max=10)])
    email = fields.Str(required=True, validate=validate.Email(error="not a valid email address"))
    password = fields.Str(required=True, validate=[validate.Length(min=6, max=36)], load_only=True)
    joined_on = fields.DateTime(dump_only=True)

    """meta is needed for formatting json returns"""

    class Meta:
        fields = ('id', 'username', 'email')


@pre_load
def process_input(self, data):
    data['email'] = data['email'].lower.strip()
    data['username'] = data['username'].lower.strip()
    return data


class JokeSchema(Schema):
    class Meta:
        fields = ('user_id', 'body')


"""for future reference"""
# user_schema = UserSchema()
# users_schema = UserSchema(many=True)
# This part defined structure of response of our endpoint. We want that all of our endpoint will have JSON response. Here we define that our JSON response will have two keys(username, and email). Also we defined user_schema as instance of UserSchema, and user_schemas as instances of list of UserSchema.
