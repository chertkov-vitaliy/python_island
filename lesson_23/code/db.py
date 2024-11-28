import psycopg2
import config

class DB:
    def __init__(self, host, port, user, passwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn  = self.connect()

    def connect(self):
        try:

            return psycopg2.connect(
                user=self.user,
                password=self.passwd,
                host=self.host,
                port=self.port,
                database=self.db
            )


        except psycopg2.OperationalError as e:
            print("I am unable to connect to the database")
            print(e)


    def insert_all(self, sql, data):
        pass

    def insert_one(self, sql, data):
        pass

    def execute(self, sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)

        except Exception as e:
            print(e)
        else:
            self.conn.commit()

    def update(self):
        pass

    def delete(self):
        pass

SQL_CREATE_TABLE_TEST = "CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);"
db = DB(config.host, config.port, config.user, config.passwd, config.db)
db.execute(SQL_CREATE_TABLE_TEST)

