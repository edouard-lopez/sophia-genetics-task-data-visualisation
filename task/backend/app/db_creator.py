import sqlite3
from sqlite3 import Error
import os

# # from pprint import pprint

from json_parser import JsonParser


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param connection: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_users_usage(connection, user_usage):
    """
    Create a new user usage into the user_usage table
    :param connection:
    :param user_usage:
    :return: user_usage id
    """
    cursor = connection.cursor()
    for usage in user_usage:
        new_usage = {
            "salesforceId": usage.get("salesforceId"),
            "predictedUsage": str(usage.get("predictedUsage")),  # ugly trick
            "actualUsage": str(usage.get("actualUsage")),
        }
        # pprint(new_usage)
        cursor.execute(
            """ 
                INSERT OR IGNORE INTO user_usage(predicted_usage,actual_usage,salesforce_id)
                VALUES(:salesforceId, :predictedUsage, :actualUsage)
            """,
            new_usage,
        )
    return cursor.lastrowid


def insert_users(connection, users):
    """
    Insert user from JSON
    :param connection:
    :param user:
    :return:
    """
    cursor = connection.cursor()
    for user in users:
        cursor.execute(
            """
                INSERT OR IGNORE INTO users(id, country, name, owner, manager)
                VALUES(:salesforceId, :country, :name, :owner, :manager)
            """,
            user,
        )
    return cursor.lastrowid


def setup_tables(connection):
    SQL_CREATE_USER_USAGE_TABLE = """CREATE TABLE IF NOT EXISTS user_usage (
                                        id integer PRIMARY KEY,
                                        predicted_usage text NOT NULL,
                                        actual_usage text NOT NULL,
                                        salesforce_id integer NOT NULL,
                                        FOREIGN KEY (salesforce_id) REFERENCES users (id)
                                    ); """

    SQL_CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY, 
                                        country text NOT NULL,
                                        name text NOT NULL,
                                        owner text NOT NULL,
                                        manager text NOT NULL
                                );"""
    if connection is not None:
        create_table(connection, SQL_CREATE_USER_USAGE_TABLE)
        create_table(connection, SQL_CREATE_USERS_TABLE)


if __name__ == "__main__":
    CURRENT_DIRECTORY = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__))
    )
    DB_FILE = os.path.join(CURRENT_DIRECTORY, "data.db")

    connection = create_connection(DB_FILE)
    with connection:
        setup_tables(connection)
        insert_users(connection, JsonParser().domainY())
        insert_users_usage(connection, JsonParser().user_usage())
