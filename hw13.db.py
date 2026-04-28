import sqlite3
connection = sqlite3.connect('hw13.db')

with open("schema.sql") as file:
    connection.executescript(file.read())

connection.close()