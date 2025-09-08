from utils.client import Client
from pydantic import BaseModel


class TokenPair(BaseModel):
    access_token: str
    token_type: str


class UserAccessToken(BaseModel):
    grant_type: str = "password"
    username: str
    password: str
    scope: str | None = None
    client_id: str | None = None
    client_secret: str | None = None


class LoginClient:
    def __init__(self, client: Client):
        self.client = client

    def get_access_token(self, user: UserAccessToken):
        return self.client.request(
            method="POST",
            url="/api/v1/login/access-token",
            data=user.model_dump(exclude_none=True),
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
