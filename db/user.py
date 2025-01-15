from config.db import execute

def add_user(firstname, lastname):
    execute('''
        INSERT INTO users (firstname, lastname)
        VALUES (%s, %s)
    ''', (firstname, lastname))

    print(get_users())

def get_users():
    rows = execute("SELECT id, firstname, lastname FROM users")
    return rows.fetchall()

