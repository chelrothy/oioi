from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import SQLAlchemyError

from model import session
from model.user import User


def sign_up(id, password, name):

    try:
        user = session.query(User).filter(User.id == id).first()

        if user:
            return abort(409, "This email is already sign up")

        add_user = User(id=id, password=generate_password_hash(password), name=name)

        session.add(add_user)
        session.commit()

        return {
            "message": "Successfully signed up"
        }, 201

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "database_error")


def login(id, password):

    try:
        user = session.query(User).filter(User.id == id).first()
        check_user_pw = check_password_hash(user.password, password) if user else None

        if check_user_pw:

            access_token = create_access_token(identity=id)

            return {
                "access_token": access_token
            }

        else:
            return abort(400, "The email or password is incorrect")

    except SQLAlchemyError:
        session.rollback()
        return abort(500, "database_error")
