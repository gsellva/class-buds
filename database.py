import os
import sqlite3

DATABASE_NAME = os.environ.get('DATABASE_PATH', 'tutors.db')


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row
    # Keep foreign-key relationships enabled for each connection.
    connection.execute('PRAGMA foreign_keys = ON')
    return connection


def _column_names(connection, table_name):
    return {
        column['name']
        for column in connection.execute(f'PRAGMA table_info({table_name})').fetchall()
    }


def init_database():
    connection = get_connection()

    connection.execute('''
        CREATE TABLE IF NOT EXISTS tutors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            grade TEXT NOT NULL,
            school TEXT NOT NULL,
            subject TEXT NOT NULL,
            bio TEXT NOT NULL,
            availability TEXT NOT NULL,
            contact TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    connection.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            student_contact TEXT NOT NULL DEFAULT '',
            tutor_id INTEGER NOT NULL,
            preferred_time TEXT NOT NULL,
            message TEXT,
            status TEXT NOT NULL DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (tutor_id) REFERENCES tutors(id)
        )
    ''')

    # Migrate databases created before request approval was added.
    request_columns = _column_names(connection, 'requests')
    if 'status' not in request_columns:
        connection.execute(
            "ALTER TABLE requests ADD COLUMN status TEXT NOT NULL DEFAULT 'pending'"
        )

    # Migrate databases created before students gave a WhatsApp number.
    if 'student_contact' not in request_columns:
        connection.execute(
            "ALTER TABLE requests ADD COLUMN student_contact TEXT NOT NULL DEFAULT ''"
        )

    connection.execute('''
        CREATE TABLE IF NOT EXISTS impact_stories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quote TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    connection.commit()
    connection.close()
