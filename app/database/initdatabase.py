import sqlite3

def execute_sql_queries(cursor: sqlite3.Cursor):
    cursor.execute("""
        DROP TABLE IF EXISTS Users;
    """)
    cursor.execute("""
        CREATE TABLE Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nom TEXT NOT NULL,
            Prénom TEXT NOT NULL,
            Login TEXT UNIQUE NOT NULL,
            Password TEXT NOT NULL
            Password_hash TEXT NOT NULL,
            Role TEXT NOT NULL
        );
    """)
    cursor.execute("""
        INSERT INTO Users (Nom, Prénom, Login, Password, Password_hash, Role)
        VALUES 
            ('John', 'Doe', 'JDoe','JDoe1', '3f79cbd1480d8e02e9c2cc366c90caa09d31dd7d', 'User'),
            ('Valentin', 'Dujardin', 'ValDuj','motdepasse', '940c0f26fd5a30775bb1cbd1f6840398d39bb813', 'Admin');
    """)
