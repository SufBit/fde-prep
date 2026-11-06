import sqlite3

def create_table(conn):
    # CREATE TABLE IF NOT EXISTS repos (...5 columns...)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS repos (
            name TEXT,
            language TEXT,
            description TEXT,
            updated_at TEXT,
            stars INTEGER
        )
    """)

def insert_repos(conn, repos: list[dict]):
    # empty the table, insert each repo with ? placeholders, commit once
    ...
    conn.execute("DELETE FROM repos")
    for repo in repos:
        conn.execute("INSERT INTO repos VALUES (?, ?, ?, ?, ?)", 
                     (repo['name'], repo['language'], repo['description'], repo['updated_at'], repo['stars']))
    conn.commit()