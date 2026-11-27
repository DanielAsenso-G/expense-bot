import sqlite3

DB_PATH = "expenses.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            note TEXT,
            created_at TEXT NOT NULL DEFAULT (datetime('now'))
        )
        """
    )

    conn.commit()
    conn.close()

def add_expense(amount, category, note=None):
    conn = get_connection()
    conn.execute(
        "INSERT INTO expenses (amount,category, note) VALUES (?, ?, ?)",
        (amount, category, note)
    )

    conn.commit()
    conn.close()

def get_expenses():
    conn = get_connection()
    cursor = conn.execute(
        "SELECT * FROM expenses ORDER BY created_at DESC"
    )
    rows = cursor.fetchall()
    conn.close()
    return rows