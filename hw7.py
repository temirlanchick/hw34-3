import sqlite3

db = sqlite3.connect('students')

students = db.cursor()

students.execute('''CREATE TABLE IF NOT EXISTS студент (
    id INT AUTO_INCREMENT PRIMARY KEY,
    хобби TEXT,
    имя TEXT,
    фамилия TEXT,
    год_рождения INTEGER,
    баллы_за_дз INTEGER
)''')

students.execute('''INSERT INTO студент (хобби, имя, фамилия, год_рождения, баллы_за_дз)
VALUES
    ('Компьютеры', 'Иван', 'Иванович', 1995, 15),
    ('Рисование', 'Мария', 'Петровна', 1998, 8),
    ('Футбол', 'Петр', 'Сидоров', 1997, 12),
    ('Кино', 'Анна', 'Кузнецова', 2000, 9),
    ('Музыка', 'Алексей', 'Петров', 1999, 14),
    ('Литература', 'Ольга', 'Смирнова', 1996, 7),
    ('Театр', 'Артем', 'Иванов', 1994, 11),
    ('Химия', 'Екатерина', 'Козлова', 2001, 16),
    ('Математика', 'Дмитрий', 'Федоров', 1993, 18),
    ('История', 'София', 'Морозова', 1992, 6);
''')

students.execute('''SELECT * FROM студент WHERE LENGTH(фамилия) > 10;''')

students.execute('''UPDATE студент SET имя = 'genius' WHERE баллы_за_дз > 10;
''')
students.execute('''SELECT * FROM студент WHERE имя = 'genius';
''')
students.execute('''DELETE FROM студент WHERE id % 2 = 0;
''')


db.commit()
db.close()