class Config():
    def __init__(self, env):
        if env is 'Dev':
            self.app_env = {
                'POSTGRES_URL': 'postgresql://schroder@localhost:5432/',
                'POSTGRES_PWORD': 'change this shit',
                'POSTGRES_DB': 'fschk',
                'MONGOURL': '',
                'MONGOPWORD': ''
            }
        elif env is 'Stage':
            self.app_env = {
                'POSTGRESURL': '',
                'POSTGRESPWORD': '',
                'POSTGRES_DB': 'fschk',
                'MONGOURL': '',
                'MONGOPWORD': ''
            }
        elif env is 'Prod':
            self.app_env = {
                'POSTGRESURL': '',
                'POSTGRESPWORD': '',
                'POSTGRES_DB': 'fschk',
                'MONGOURL': '',
                'MONGOPWORD': ''
            }

        return self


if __name__ == '__main__':
    pass
