CREATE TABLE IF NOT EXISTS vault_records (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL, username TEXT NOT NULL, secret_value TEXT NOT NULL,
  notes TEXT DEFAULT '', created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Create (use placeholders in application code)
INSERT INTO vault_records(title, username, secret_value, notes)
VALUES ('Demo Account', 'demo_user', 'demo-only-value', 'sample');

-- Search
SELECT id, title, username, notes FROM vault_records
WHERE title LIKE '%Demo%' OR username LIKE '%demo%';

-- Update
UPDATE vault_records SET notes='updated sample' WHERE id=1;

-- Delete
DELETE FROM vault_records WHERE id=1;
