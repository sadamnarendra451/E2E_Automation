import sqlite3


def test_database_connection():
    conn = sqlite3.connect('test_database.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, status TEXT)''')
    cursor.execute("INSERT INTO logs (status) VALUES ('SUCCESS')")
    conn.commit()

    cursor.execute("SELECT * FROM logs")
    result = cursor.fetchall()
    assert len(result) > 0
    conn.close()