
from flask import Flask, request, redirect, url_for, render_template
import sqlite3
app = Flask(__name__)
def init_db():
    with sqlite3.connect('notes.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)')
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        with sqlite3.connect('notes.db') as conn:
            conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        return redirect(url_for('index'))
    with sqlite3.connect('notes.db') as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)
if __name__ == '__main__':
    init_db()
    app.run(debug=True)