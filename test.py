import sqlite3

mydb = sqlite3.connect("data.db")

cursor = mydb.cursor()

# cursor.execute("Delete FROM  passw")
# # cursor.execute("INSERT INTO passw (site, username, password) VALUES" + "('nse.in', 'kite', '3rfcaw')")
# mydb.commit()

cursor.execute("SELECT * FROM  passw")

for passws in cursor.fetchall():
    print(passws)
