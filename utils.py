import hashlib


class Response:
    def __init__(self, data: str, status_code: int):
        self.data = data
        self.status_code = status_code

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def match_password(hashed_password, user_password):
        return hashed_password == hashlib.sha256(user_password.encode()).hexdigest()


hashed = Response.hash_password("my_password")
is_match = Response.match_password(hashed, "my_password")
print(f"Hashed password: {hashed}")
print(f"Password match: {is_match}")
