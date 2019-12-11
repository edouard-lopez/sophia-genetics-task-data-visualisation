import sqlite3
from sqlite3 import Error
import json
import os


class DBProvider:
    def __init__(self):
        self.connection = None
        CURRENT_DIRECTORY = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )
        self.DB_FILE = os.path.join(CURRENT_DIRECTORY, "data.db")
        self.create_connection()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            column_name = col[0]
            d[column_name] = row[idx]
            if column_name == 'predicted_usage' or column_name == 'actual_usage':
                d[column_name] = json.loads(row[idx])
        return d

    def create_connection(self):
        """ create a database connection to the SQLite database
        :return: Connection object or None
        """
        try:
            self.connection = sqlite3.connect(self.DB_FILE)
            self.connection.row_factory = self.dict_factory
            return self.connection
        except Error as e:
            print(e)

    def user_usage(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from user_usage")
        rows = cursor.fetchall()

        return rows

    def domainY(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * from users")
        rows = cursor.fetchall()

        return rows
