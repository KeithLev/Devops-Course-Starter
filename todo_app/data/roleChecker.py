from flask_login import current_user
from flask import redirect
import os

def ReadWriteNeeded(func):
    def wrapper(*args, **kwargs):
        if current_user.role == 'Read/Write' or os.getenv('LOGIN_DISABLED') == 'True':
            return func(*args, **kwargs)
        else: return redirect('/')
    wrapper.__name__ = func.__name__
    return wrapper
