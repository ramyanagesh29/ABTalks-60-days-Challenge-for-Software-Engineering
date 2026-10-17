import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("secret_vault.db")

def connect():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("""CREATE TABLE IF NOT EXISTS vault_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        username TEXT NOT NULL,
        secret_value TEXT NOT NULL,
        notes TEXT DEFAULT '',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    )""")
    return db

def add_record(title, username, secret_value, notes=""):
    with connect() as db:
        cur = db.execute("INSERT INTO vault_records(title, username, secret_value, notes) VALUES(?,?,?,?)",
                         (title, username, secret_value, notes))
        return cur.lastrowid

def search_records(term):
    with connect() as db:
        rows = db.execute("SELECT id,title,username,notes,created_at FROM vault_records "
                          "WHERE title LIKE ? OR username LIKE ? ORDER BY title",
                          (f"%{term}%", f"%{term}%")).fetchall()
        return [dict(row) for row in rows]

def get_record(record_id):
    with connect() as db:
        row = db.execute("SELECT * FROM vault_records WHERE id=?", (record_id,)).fetchone()
        return dict(row) if row else None

def update_record(record_id, **fields):
    allowed = {"title", "username", "secret_value", "notes"}
    changes = {k: v for k, v in fields.items() if k in allowed and v is not None}
    if not changes:
        return False
    sql = "UPDATE vault_records SET " + ", ".join(f"{k}=?" for k in changes) + " WHERE id=?"
    with connect() as db:
        cur = db.execute(sql, (*changes.values(), record_id))
        return cur.rowcount > 0

def delete_record(record_id):
    with connect() as db:
        cur = db.execute("DELETE FROM vault_records WHERE id=?", (record_id,))
        return cur.rowcount > 0

if __name__ == "__main__":
    rid = add_record("Demo Account", "demo_user", "demo-only-secret", "sample")
    print("Secret Vault Database")
    print("Added record ID:", rid)
    print("Search results:", search_records("Demo"))
    update_record(rid, notes="updated sample note")
    print("Updated record:", get_record(rid))
    print("Deleted:", delete_record(rid))
    print("Search after delete:", search_records("Demo"))
