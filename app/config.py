import os


class Environment(env):
    def __init__(self, env):
        self.app_env = {
            'Dev': {
                'ABS_PATH_TO_APP': os.getcwd(),
                'POSTGRESURL': '',
                'POSTGRESPWORD': '',
                'MONGOURL': '',
                'MONGOPWORD': ''
            },
            'Stage': {
                'POSTGRESURL': '',
                'POSTGRESPWORD': '',
                'MONGOURL': '',
                'MONGOPWORD': ''
            },
            'Prod': {
                'POSTGRESURL': '',
                'POSTGRESPWORD': '',
                'MONGOURL': '',
                'MONGOPWORD': ''
            }
        }



if __name__ == '__main__':
    pass
