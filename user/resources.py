# coding: utf-8
from __future__ import absolute_import

from flask import Blueprint
from flask_restful import Api, Resource, reqparse, abort
from flask.ext.login import login_user, logout_user
from user.model import User


user_blueprint = Blueprint('user', __name__)
api = Api(user_blueprint)


@api.resource('/user/logout/')
class UserLogoutResource(Resource):

    def get(self):
        logout_user()


@api.resource('/user/login/')
class UserLoginResource(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', required=True, type=str)
        parser.add_argument('password', required=True, type=str)
        args = parser.parse_args()
        email = args.get("email")
        password = args.get("password")

        user = User.get_user_by_email(email)
        if user.check_password(password):
            login_user(user)
            return 200
        abort(401)


@api.resource('/user/', '/user/<string:email>')
class UserResource(Resource):

    def get(self, email=None):
        parser = reqparse.RequestParser()
        parser.add_argument('limit', type=int)
        args = parser.parse_args(strict=True)
        limit = args.get('limit')

        if limit is not None:
            users = User.limit_users(limit)
            return [user.to_dict() for user in users]
        elif email is not None:
            user = User.get_user_by_email(email)
            return user.to_dict()

        abort(400, message="You must provide limit or email")

    def post(self):
        pass

    def delete(self, id=None):
        pass

    def put(self, id=None):
        pass
