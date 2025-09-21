import sqlite3

# Path to the database file
DB_PATH = "backend/database.db"

def init_db():
    """Initialize the database and create tables if they don't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Appointments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            doctor TEXT NOT NULL,
            datetime TEXT NOT NULL,
            email TEXT ,
            status TEXT DEFAULT 'scheduled'
        )
    ''')

    # Optional: FAQ logs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faq_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Database initialized successfully!")
