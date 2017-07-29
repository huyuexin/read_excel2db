import sqlite3
connection = sqlite3.connect('test.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE newdate (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                names text NOT NULL)""")
connection.commit()
connection.close()
