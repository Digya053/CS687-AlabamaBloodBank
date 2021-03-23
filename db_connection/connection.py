import MySQLdb
import yaml

class Connection:
    def __init__(self):
        yamlfile = 'config/mysql_config.yaml'
        
        with open(yamlfile, "r") as yamlfile:
            data = yaml.load(yamlfile, Loader=yaml.FullLoader)

            self.host = data[0]['dbinfo']['dbhost']
            self.user = data[0]['dbinfo']['dbusername']
            self.password = data[0]['dbinfo']['dbpassword']
            self.database = data[0]['dbinfo']['database']

            try:
                self.db = MySQLdb.connect(self.host, self.user, self.password, self.database)
                print("Connected to batabase " + self.database)
            except:
                print("Can't connect to database " + self.database)
                return 0

            self.cursor = self.db.cursor()

    def execute_command(self, query):
        self.cursor.execute(query)

    def close_connection(self):
        self.db.close()

    def commit_changes(self):
        self.db.commit()

    def fetch_one(self):
        return self.cursor.fetchone()

    def fetch_all(self):
        return self.cursor.fetchall()


conn = Connection()
