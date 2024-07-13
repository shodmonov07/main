from utils import hash_password, match_password


class User:
    def __init__(self, username, password):
        self.username = username
        self.hashed_password = hash_password(password)

    def verify_password(self, password):
        return match_password(self.hashed_password, password)


def register_user(username, password):
    new_user = User(username, password)
    print(f"User {username} registered with hashed password {new_user.hashed_password}")
    return new_user


def login_user(username, password, registered_users):
    for user in registered_users:
        if user.username == username and user.verify_password(password):
            print(f"User {username} logged in successfully")
            return True
    print("Invalid username or password")
    return False


if __name__ == "__main__":
    registered_users = []

    user1 = register_user("jamolbek123", "1234")
    registered_users.append(user1)

    login_user("ali123", "12345", registered_users)
    login_user("jamoliddin1234", "123456", registered_users)
    login_user("robiya123", "1234567", registered_users)