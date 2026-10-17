# Day 53 — The Secret Vault Database

SQLite CRUD system:
- Create: `add_record`
- Search: `search_records`
- Read one: `get_record`
- Update: `update_record`
- Delete: `delete_record`

SQL values use parameterized queries. Search results omit the secret field by default.

**Security warning:** this is a learning CRUD demo, not a production password manager. The example stores
secret values as plain text. Do not enter real passwords or API keys. Production secret storage needs
encryption at rest, secure key management, access control, safe logging and security review.

Run: `python secret_vault.py`. The SQLite file is created beside the script.
