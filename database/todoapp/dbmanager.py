import pymysql.cursors as cursors
import pymysql



class Db_Guru:

    def __init__(self, host, user, db, password = "" ):
        self.host = host
        self.database = db
        self.user = user
        self.password = password

    def connect(self):
        
        Connection = pymysql.Connection(
                                host = self.host,
                                user = self.user,
                                password = self.password,
                                database = self.database,
                                cursorclass = pymysql.cursors.DictCursor # Optional
                            )

        return Connection

    def read(self, command):

        Connection = self.connect()

        with Connection.cursor() as cursor:
            cursor.execute(command)
            return cursor.fetchall()

    def write(self, command):

        Connection = self.connect()

        with Connection.cursor() as cursor:

            cursor.execute(command)
            Connection.commit()
            return True