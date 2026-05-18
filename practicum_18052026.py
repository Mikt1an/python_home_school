import os

import pymysql
import dotenv
dotenv.load_dotenv()

class HR:
    def __init__(self):
        self.__config = {"host": os.getenv("DB_HOST"),
                         "user": os.getenv("DB_USER"),
                         "password": os.getenv("DB_PASSWORD"),
                         "database": os.getenv("DB_NAME")
                         }
        print(self.__config)

    def __enter__(self):
        self.__conn = pymysql.connect(**self.__config)
        self.__cursor = self.__conn.cursor()
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__conn.close()
        print("__exit__")
        return False

    def __execute(self, sql, params = None):
        self.__cursor.execute(sql, params)
        return self.__cursor.fetchall()

    def get_employers(self, depart=None):
        text = """
               SELECT e.first_name, e.last_name, e.salary, d.department_name, j.job_title 
                  FROM employees as e
                   JOIN departments as d ON d.department_id = e.department_id
                   JOIN jobs as j ON j.job_id = e.job_id
                   WHERE d.department_name = %(depart)s OR %(depart)s = 1
                   ORDER BY e.salary desc
               """
        yield from self.__execute(text, {"depart": depart} if depart else {"depart":1})

    def get_department(self):
        text = """
                SELECT d.department_name
                    FROM departments as d
                """
        return self.__execute(text)



hr = HR()
with hr as hr:
    temp_department = hr.get_department()
    for _N, (dep,) in enumerate(temp_department, start=1):
        print(_N, dep)
    input_us = int(input("Enter department number: "))
    prnt = temp_department[input_us-1][0]
    print(prnt)
    # print(hr.get_employers(depart=prnt))
    for _N, (first_name, last_name, salary, department, title) in enumerate(hr.get_employers(depart=prnt), start=1):
        print(f"{_N} | {first_name} {last_name} | {salary} | {department} | {title}")





