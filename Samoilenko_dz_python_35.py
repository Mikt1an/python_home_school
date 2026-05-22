# 1

class User:
    """
    User class with validation and user counter.
    """
    total_users = 0
    def __init__(self, username, password):

        if not isinstance(username, str) or username.strip() == "":
            raise ValueError("username must be a string")
        if not isinstance(password, str) or len(password) < 5:
            raise ValueError("Password must be a string with at least 5 characters")
        self.username = username
        self.password = password
        User.total_users += 1

    def __str__(self):
        return f"Username: {self.username}"

    @classmethod
    def print_user(cls):
        return cls.total_users

try:
    us1 = User("", "12345")
except ValueError as e:
    print("Error: ", e)

try:
    us1 = User("Anton", "1")
except ValueError as e:
    print("Error: ", e)

try:
    us1 = User("Anton", "123456")
    us2 = User("Max", "1234536")
    us3 = User("Eva", "12954845")
    print(us1)
    print(us2)
    print(us3)
    print("Total user: ", User.print_user())
except ValueError as e:
    print("Error: ", e)


