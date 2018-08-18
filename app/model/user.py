import jwt
import datetime
from config import get_env


class User:

    def __init__(self, name, email, password, is_admin=False):
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def get_token(self):
        return jwt.encode({
            'name': self.name,
            'email': self.email,
            'isAdmin': self.is_admin,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(days=int(get_env('AUTH_TOKEN_EXPIRY_DAYS')),
                                                                   seconds=int(get_env('AUTH_TOKEN_EXPIRY_SECONDS'))),
        }, get_env('APP_SECRET'), algorithm='HS256').decode("utf-8")

    @staticmethod
    def decode(token):
        try:
            payload = jwt.decode(token, get_env('APP_SECRET'), algorithms='HS256')
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired, Please sign in again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please sign in again'
