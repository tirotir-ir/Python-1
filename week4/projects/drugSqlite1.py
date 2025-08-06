import sqlite3

def init_db():
    conn = sqlite3.connect('medication_reminder.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY,
            medication_name TEXT NOT NULL,
            dosage TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()
