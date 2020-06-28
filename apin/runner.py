"""apin runner"""
from apin.client import Client
from apin.format import Case
from apin.validation import Response


class Runner:
    def __init__(self):
        self.case = None
        self.client = Client()

    def run(self, file):
        case = Case.from_yaml(file)
        client_resp = self.client.request(**case.request_data)
        resp = Response(client_resp)
        for validator in case.data["validators"]:
            resp.assert_that(validator)


if __name__ == '__main__':
    Runner().run('../samples/test_ref.yml')
