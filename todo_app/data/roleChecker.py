from flask_login import current_user
from flask import redirect
import os

def ReadWriteNeeded(func):
    def wrapper(*args, **kwargs):
        if os.getenv('LOGIN_DISABLED') == 'True' or current_user.role == 'Read/Write':
            return func(*args, **kwargs)
        else: return "Not authorised", 401
    wrapper.__name__ = func.__name__
    return wrapper
