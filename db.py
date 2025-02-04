import sqlite3
from flask import g, Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)

if __name__ =="__main__":
    app.run(debug=True)

conn = sqlite3.connect('RZA.db', check_same_thread=False)
cursor = conn.cursor()

def add_user(fname, lname, email, password):
    cursor.execute("INSERT INTO users (FirstName, LastName, Email, Password) VALUES (?, ?, ?, ?)", (fname, lname, email, password))
    conn.commit()
    conn.close()

def verify_user(email, password):
    cursor.execute("SELECT * FROM users WHERE Email = ? AND Password = ?", (email, password))
    user = cursor.fetchone()
    return user