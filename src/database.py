import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to database: {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table for storing user greetings."""
    try:
        sql_create_greetings_table = """CREATE TABLE IF NOT EXISTS greetings (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            greeting text NOT NULL
                                        );"""
        cursor = conn.cursor()
        cursor.execute(sql_create_greetings_table)
    except sqlite3.Error as e:
        print(e)

def insert_greeting(conn, name, greeting):
    """Insert a new greeting into the greetings table."""
    sql = '''INSERT INTO greetings(name, greeting)
             VALUES(?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, (name, greeting))
    conn.commit()
    return cursor.lastrowid

def fetch_greetings(conn):
    """Fetch all greetings from the greetings table."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM greetings")
    rows = cursor.fetchall()
    return rows