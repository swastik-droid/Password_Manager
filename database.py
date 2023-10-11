import sqlite3


class Database:
    def __init__(self):
        # connecting to the database and setting up a cursor object
        self.mydb = sqlite3.connect("data.db")
        self.cursor = self.mydb.cursor()

        # using the execute method to create a table as per requirements.
        table = "CREATE TABLE IF NOT EXISTS passw (site varchar(255), " \
                "username varchar(255), password varchar(255)," \
                "ID INTEGER PRIMARY KEY AUTOINCREMENT)"
        self.execute(command=table, commit=True)

    # this is method for executing any command to the database
    def execute(self, command, commit=False):
        self.cursor.execute(command)

        # only required when the operation needs commit
        if commit:
            self.mydb.commit()
