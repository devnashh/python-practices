import mysql.connector

class Todo:

    def __init__(self):
     self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "todo_db"
    )
     self.cursor = self.conn.cursor()

    def add_task(self, activity, status):
       sql = "INSERT INTO task (activity, status) VALUES (%s, %s)"
       value = (activity, status)

       self.cursor.execute(sql, value)
       self.conn.commit()

       print("New activity successfully ADDED to the database!")

    def update_task(self, id, new_activity, new_status):
       sql = "UPDATE task SET activity= %s, status = %s WHERE id = %s"
       values = (new_activity, new_status, id)
       self.cursor.execute(sql, values)
       self.conn.commit()

       print("Activity successfully UPDATED to the database!")

    def delete_task(self, id):
       sql = "DELETE FROM task WHERE id = %s"
       values = (id, )
       self.cursor.execute(sql, values)
       self.conn.commit()

       print("Activity has been DELETED to the database!")

    def show_task(self):
       sql = "SELECT * FROM task"
       self.cursor.execute(sql)
       result = self.cursor.fetchall()

       for row in result:
          print(row)
    def close_conn(self):
       self.conn.close()
       print("Connection closed successfully!")

act = Todo()

act.delete_task(2)

act.show_task()


act.close_conn()
