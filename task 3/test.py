import os
import sqlite3
import hashlib

# ❌ Hardcoded database password
DB_PASSWORD = "admin123"

def connect_db():
    # ❌ Storing password directly in code
    conn = sqlite3.connect("users.db")
    return conn

def create_user_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    # ❌ Weak password hashing (MD5)
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
    conn.commit()
    conn.close()

def login_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    #  SQL injection risk (string formatting instead of parameterized queries)
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{hashlib.md5(password.encode()).hexdigest()}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def run_command():
    user_input = input("Enter a command to run: ")
    #  Dangerous command execution
    os.system(user_input)

if __name__ == "__main__":
    create_user_table()
    print("1. Register\n2. Login\n3. Run Command")
    choice = input("Choose: ")

    if choice == "1":
        u = input("Username: ")
        p = input("Password: ")
        register_user(u, p)
        print("User registered ")

    elif choice == "2":
        u = input("Username: ")
        p = input("Password: ")
        if login_user(u, p):
            print("Login successful ")
        else:
            print("Login failed ")

    elif choice == "3":
        run_command()