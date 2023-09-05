import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\user\Desktop\tic atelier\Voting System\public\db\voting.db"

    sql_create_nominees_table = """ CREATE TABLE IF NOT EXISTS nominees (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        competition text NOT NULL,
                                        category text NOT NULL,
                                        begin_date text
                                    ); """

    sql_create_voters_table = """ CREATE TABLE IF NOT EXISTS voters (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        voter_id text NOT NULL UNIQUE,
                                        begin_date text
                                    ); """

    sql_create_votes_table = """CREATE TABLE IF NOT EXISTS votes (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    category text NOT NULL,
                                    competition text NOT NULL,
                                    nominee_id integer NOT NULL,
                                    voter_id text NOT NULL,
                                    begin_date text
                                );"""

    sql_create_competition_table = """CREATE TABLE IF NOT EXISTS competition (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    category text NOT NULL,
                                    competition text NOT NULL,
                                    begin_date text
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        c = conn.cursor()
        c.execute("DROP TABLE nominees")
        # create nominees table
        create_table(conn, sql_create_nominees_table)

        # create voters table
        create_table(conn, sql_create_voters_table)

        # create votes table
        create_table(conn, sql_create_votes_table)

        # create competition table
        create_table(conn, sql_create_competition_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
