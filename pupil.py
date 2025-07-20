import mysql.connector

class PupilProfile:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "student_db"
        )
        self.cursor = self.conn.cursor()

    def add_pupil(self, name, age):
        sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
        values = (name, age)

        self.cursor.execute(sql, values)
        self.conn.commit()

        print(f"{name}, Has been successfully added to the database!")

    def update_pupil(self, id, new_name, new_age):
        sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
        values = (new_name, new_age, id)

        self.cursor.execute(sql, values)
        self.conn.commit()
        
        print(f"{new_name} Pupil updated successfully!")
        print(f"Name: {new_name}")
        print(f"Age: {new_age}")

    def delete_pupil(self, id):
        sql = "DELETE FROM students WHERE id = %s"
        values = (id,)

        self.cursor.execute(sql, values)
        self.conn.commit()

        print(f"Pupil {id} Has been Deleted!")

    def get_pupil(self):
        sql = "SELECT * FROM students"
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
       
        print("List of all database informations of PUPILS")
        for row in results:
            print(row)
    
    def close_conn(self):
        self.conn.close()
        print(f"Connection closed!")


pupil = PupilProfile()

pupil.update_pupil(2, "kopoIdollss", 1010)
pupil.delete_pupil(6)
pupil.get_pupil()


pupil.close_conn()