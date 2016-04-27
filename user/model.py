# coding: utf-8

# This module should  only have operations on
# database level

from app import db


class User(db.Model):

    __tablename__ = 'users'
    session = db.session
    is_active = db.Column(db.Boolean, default=True)
    is_anonymous = db.Column(db.Boolean, default=False)
    admin = db.Column(db.Boolean)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80))
    gender = db.Column(db.String(20))
    is_authenticated = db.Column(db.Boolean, default=False)

    def __init__(self, name, email, password, gender, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.gender = gender
        self.active = True
        self.admin = is_admin

    def to_dict(self):
        return {
            'is_admin': self.admin,
            'is_active': self.active,
            'name': self.name
        }

    def get_id(self):
        return self.email

    def is_active(self):
        return self.is_active

    def is_admin(self):
        return self.admin

    @classmethod
    def delete_user(cls, email):
        cls.session.query(cls).filter(cls.email == email).delete()
        cls.session.commit()

    @classmethod
    def limit_users(cls, limit):
        return cls.session.query(cls).filter(limit)

    @classmethod
    def get_all(cls):
        return cls.session.query(cls).all()

    @classmethod
    def save(cls, user):
        cls.session.add(user)
        cls.session.commit()
        return user

    @classmethod
    def get_user_by_email(cls, email):
        return cls.session.query(cls).get(email)

    def authentic(self):
        self.is_authenticated = True
        User.session.commit()

    def unauthentic(self):
        self.is_authenticated = False
        User.session.commit()
