import random
import string


class Application:
    users = {}
    requests = []

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

    def add_request(self, request):
        self.requests.append(request.get_dict())

    @staticmethod
    def generate_random_key():
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
