import mysql.connector

class Bike:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host ="localhost",
            user = "root",
            password = "",
            database = "student_db"
        )
        self.cursor = self.conn.cursor()
        print("DataBase Connection Opened!")

    def add_bike(self, name, age):
        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        values = (name, age)
        self.cursor.execute(sql, values)
        self.conn.commit()
        print(f"Added student info, ID: {name}, ID: {self.cursor.lastrowid}")

    def get_bikes(self):
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        print("All informations")
        for row in result:
            print(row)

    def close_conn(self):
        self.conn.close()
        print("Connection Closed!")

bikes = Bike()

bikes.add_bike("Toseek", 2)

bikes.get_bikes()

bikes.close_conn()