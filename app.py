from flask import Flask, request, jsonify, render_template_string, redirect, url_for

app = Flask(__name__)
notes = []

# Simple HTML templates embedded as strings for demo purposes
index_html = """
<!doctype html>
<title>Notes App</title>
<h1>Welcome to the Notes App</h1>
<a href="{{ url_for('show_notes') }}">View Notes</a> | 
<a href="{{ url_for('add_note_form') }}">Add Note</a>
"""

notes_html = """
<!doctype html>
<title>All Notes</title>
<h1>All Notes</h1>
<ul>
  {% for note in notes %}
    <li><strong>{{ note.title }}</strong>: {{ note.content }}</li>
  {% else %}
    <li>No notes yet!</li>
  {% endfor %}
</ul>
<a href="{{ url_for('add_note_form') }}">Add a new note</a> | 
<a href="{{ url_for('index') }}">Home</a>
"""

add_note_html = """
<!doctype html>
<title>Add Note</title>
<h1>Add a New Note</h1>
<form method="POST">
  <label for="title">Title:</label><br>
  <input type="text" id="title" name="title" required><br><br>
  <label for="content">Content:</label><br>
  <textarea id="content" name="content" rows="4" cols="50" required></textarea><br><br>
  <input type="submit" value="Add Note">
</form>
<a href="{{ url_for('show_notes') }}">Back to notes</a> | 
<a href="{{ url_for('index') }}">Home</a>
"""

@app.route("/")
def index():
    return render_template_string(index_html)

@app.route("/notes")
def show_notes():
    return render_template_string(notes_html, notes=notes)

@app.route("/notes/add", methods=["GET", "POST"])
def add_note_form():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        note = {
            "id": len(notes) + 1,
            "title": title,
            "content": content
        }
        notes.append(note)
        return redirect(url_for('show_notes'))
    return render_template_string(add_note_html)

# Optional: keep your existing API endpoints if you want JSON support too
@app.route("/api/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/api/notes", methods=["POST"])
def add_note_api():
    data = request.get_json()
    note = {
        "id": len(notes) + 1,
        "title": data.get("title"),
        "content": data.get("content")
    }
    notes.append(note)
    return jsonify(note), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
