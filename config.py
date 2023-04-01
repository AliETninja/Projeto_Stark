import starkbank

class Config:

    def __init__(self, project_id):
        self.project_id = project_id
        self.private_key = open('settings/private-key.pem').read()

    def connection(self):
        user = starkbank.Project(
            environment="sandbox",
            id=self.project_id,
            private_key=self.private_key
        )
        return user
