from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        if self.id == '74147088':
            self.role = 'Read/Write'
            
        else:
            self.role = 'Read'
        