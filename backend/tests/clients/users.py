from testing.utils.client import Client
from pydantic import BaseModel


class UserRegister(BaseModel):
    fullname: str
    email: str
    password: str


class UsersClient:
    def __init__(self, client: Client):
        self.client = client

    def register_user(self, user: UserRegister):
        return self.client.request(
            method="POST", url="/api/v1/users/signup", json=user.model_dump()
        )

    def get_me(self):
        return self.client.request(method="GET", url="/api/v1/users/me")

    def delete_me(self):
        return self.client.request(method="DELETE", url="/api/v1/users/me")
