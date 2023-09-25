import sqlite3

db = sqlite3.connect('game.db')

game = db.cursor()

game.execute('''CREATE TABLE IF NOT EXISTS users(
name TEXT,
age INTEGER,
password INTEGER 
)''')

game.execute('''INSERT INTO users VALUES('chupapa',69,123456)''')


db.commit()
db.close()