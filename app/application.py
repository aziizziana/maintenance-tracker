class Application:
    users = {}

    def register(self, user):
        self.users[user.email] = user

    def login(self, email, password):
        if self.users[email].password == password:
            return True
        return False

    def does_user_exist(self, email):
        if email in self.users.keys():
            return True
        return False

    def get_user(self, email):
        return self.users[email]
