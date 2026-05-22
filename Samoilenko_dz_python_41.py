# 1
import os
import pymysql
import dotenv
dotenv.load_dotenv()

class DB_WORLD:
    """
        MySQL database context manager for the World database.

        Args:
            None

        Environment variables:
            DB_HOST: Database host.
            DB_USER: Database username.
            DB_PASSWORD: Database password.
            DB_NAME_WORLD: World database name.
    """
    def __init__(self):
        self.__config = {"host": os.getenv("DB_HOST"),
                         "user": os.getenv("DB_USER"),
                         "password": os.getenv("DB_PASSWORD"),
                         "database": os.getenv("DB_NAME_WORLD"),
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
        return self.__cursor.fetchall()

class Command(DB_WORLD):
    """
        Provides SQL commands for reading countries and cities
        from the World database.
    """
    def get_country(self):
        text = """
               SELECT code, name
               FROM country
               # ORDER BY name
               """
        return self._execute(text)

    def get_cities(self, country_name = None):
        text = """
                SELECT name, population
              FROM city
              WHERE CountryCode = %s
              ORDER BY population DESC
        """
        return self._execute(text, country_name)




db = Command()
with db as db:
    temp_city = db.get_country()
    for _N, country in enumerate(temp_city, start=1):
        print(f"{_N}. {country[1]}")
    input_user = input("Enter country code or name: ")
    country_code = None
    if input_user.isdigit():
        index = int(input_user) - 1
        if 0 <= index < len(temp_city):
            country_code = temp_city[index][0]
    else:
        for country in temp_city:
            if country[1].lower() == input_user.lower():
                country_code = country[0]
                break
    if not country_code:
        print("Country not found")
    else:
        cities = db.get_cities(country_code)
        for _N, (city, population) in enumerate(cities, start=1):
            print(f"{_N}. {city} - {population}")
