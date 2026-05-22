# 1
import os
import pymysql
import dotenv
from pymysql.cursors import DictCursor
dotenv.load_dotenv()

class DB:
    """
       MySQL database context manager.

       Environment variables:
           DB_HOST_EDIT: Database host.
           DB_USER_EDIT: Database username.
           DB_PASSWORD_EDIT: Database password.
    """
    def __init__(self):
        self.__config = {"host": os.getenv("DB_HOST_EDIT"),
                         "user": os.getenv("DB_USER_EDIT"),
                         "password": os.getenv("DB_PASSWORD_EDIT"),
                         'cursorclass': DictCursor,
                         }
        print(self.__config)

    def __enter__(self):
        self.__conn = pymysql.connect(**self.__config)
        self.__cursor = self.__conn.cursor()
        print("Connection successful!")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__conn.close()
        print("__exit__")
        return False

    def _execute(self, sql, params = None):
        self.__cursor.execute(sql, params)
        # print("Executed successfully")
        return self.__cursor.fetchall()

    def _commit(self):
        self.__conn.commit()

class Command(DB):
    """
        Provides database and note management commands.
    """
    def get_show_db(self):
        text= """
        SHOW DATABASES
        """
        return self._execute(text)

    def get_show_notes(self):
        text = """
               SELECT *
               FROM notes
               """
        return self._execute(text)

    def create_database(self, db_name):
        text = f"""
                CREATE DATABASE IF NOT EXISTS {db_name}
            """
        print(f"Database {db_name} created or already exists.")
        return self._execute(text)

    def drop_table(self, db_name):
        text = f"""
                DROP TABLE IF EXISTS {db_name}
            """
        print(f"DROP TABLE {db_name}")
        return self._execute(text)

    def use_db(self, database):
        text = f"""
                USE {database}
        """
        print(f"Connecting to {database}")
        return self._execute(text)

    def create_notes_table(self):
        text = """
              CREATE TABLE IF NOT EXISTS notes (
                  id INT AUTO_INCREMENT PRIMARY KEY, 
                  title VARCHAR (255 ) NOT NULL,
                  content TEXT NOT NULL
                  ) 
              """
        print(f"Creating notes table")
        return self._execute(text)

    def delete_note_table(self, title):
        text = f"""
                DELETE FROM notes
                WHERE title = %s
                """
        print(f"Deleting {title} in table")
        return self._execute(text)

    def add_note(self, title, content):
        text = """
               INSERT INTO notes(title, content)
               VALUES (%s, %s)
               """
        self._execute(text, (title, content))
        print("Note added")
        return self._commit()

    def delete_note(self, note_id):
        text = """
               DELETE
               FROM notes
               WHERE id = %s
               """
        self._execute(text, (note_id,))
        print(f"Note with ID {note_id} deleted")
        return self._commit()


db_name = "notes_app_121225_anton_samoilenko"

try:
    c = Command()
    with c as cursor:
        c.create_database(db_name)
        c.use_db(db_name)
        c.create_notes_table()
        c.add_note("Shopping", "list")
        # print(c.get_show_db())
        print("Show notes")
        for _N, note in enumerate(c.get_show_notes(), start=1):
            print(_N, note["title"], note["content"])
except pymysql.MySQLError as e:
    print("Database error:", e)

