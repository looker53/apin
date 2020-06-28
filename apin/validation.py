"""validation response"""
import enum
import hamcrest

from typing import Any
from pydantic import BaseModel
from requests import Response as RequestsResponse


class Matchers(enum.Enum):
    equal_to = "equal_to"


class Validator(BaseModel):
    matcher: Matchers
    expected: Any
    path: Any


class Response:
    """api response."""

    def __init__(self, resp: RequestsResponse):
        self.resp = resp
        self.text = resp.text
        self.json = resp.json()

    def actual(self, path: str):
        """get the actual response by path expression.

        example:
            path: data.user.name
            return: "my_username" , resp["data"]["user"]["name"]
        """
        nodes = path.split('.')
        resp_json = self.json
        for node in nodes:
            resp_json = resp_json.get(node)
        return resp_json

    def assert_that(self, validator: dict):
        data = Validator(**validator)
        hamcrest.assert_that(
            self.actual(data.path),
            getattr(hamcrest, data.matcher.value)(data.expected)
        )


if __name__ == '__main__':
    validators = {"expected":"emo", "matcher": "equal_to", "path": "form.username"}

    from format import Case
    from client import Client

    data = Case.from_yaml('test_ref.yml')
    c = Client()
    resp = c.request(**data.request_data)

    resp = Response(resp)
    a = resp.assert_that(validators)



