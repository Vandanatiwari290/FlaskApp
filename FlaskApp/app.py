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
        if content.strip():  # Ensure non-empty content
            with sqlite3.connect('notes.db') as conn:
                conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
        return redirect(url_for('index'))
    with sqlite3.connect('notes.db') as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)
@app.route('/delete/<int:note_id>', methods=['POST'])
def delete_note(note_id):
    with sqlite3.connect('notes.db') as conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    return redirect(url_for('index'))
if __name__ == '__main__':
    init_db()
    app.run(host="0.0.0.0")
