TABLE_NAME = "Patients"
CREATE_TABLE_COMMAND = f'''
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname TEXT NOT NULL,
date_of_birth DATE,
date_of_visit DATE
)
'''

INSERT_TABLE_COMMAND = f'''
INSERT INTO {TABLE_NAME} (fullname, date_of_birth, date_of_visit) VALUES (?, ?, ?)
'''
