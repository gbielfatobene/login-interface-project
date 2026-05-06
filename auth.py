class UserList:
    def __init__(self):
        self.users = {"Gabriel": "admin123",
                       "user": "admin123",
                         "admin": "admin000"}

    def add_user(self, username, password):
        self.users[username] = password
    
    def login(self, username, password):
        return username in self.users and self.users[username] == password
    
    def registration(self, username, password):
        if username in self.users:
            return "user_exists"
        elif len(password) < 6:
            return "weak_password"
        else:
            return "registration_success"