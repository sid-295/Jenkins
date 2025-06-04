from flask import Flask, request, redirect, url_for, render_template_string

app = Flask(__name__)
notes = []

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Notes App</title>
    <style>
        body {
            font-family: "Segoe UI", sans-serif;
            background: #f4f7f8;
            padding: 30px;
            max-width: 800px;
            margin: auto;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            background: white;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 0 10px rgba(0,0,0,0.05);
            margin-bottom: 30px;
        }
        input, textarea {
            width: 100%;
            padding: 12px;
            margin-top: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 6px;
            font-size: 16px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .note {
            background: white;
            border-left: 6px solid #007bff;
            padding: 15px 20px;
            border-radius: 8px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        }
        .note h3 {
            margin: 0;
        }
    </style>
</head>
<body>
    <h1>📝 Notes App</h1>
    <form action="/add" method="POST">
        <input type="text" name="title" placeholder="Title" required>
        <textarea name="content" placeholder="Write your note here..." rows="4" required></textarea>
        <button type="submit">Add Note</button>
    </form>

    {% for note in notes %}
        <div class="note">
            <h3>{{ note.title }}</h3>
            <p>{{ note.content }}</p>
        </div>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, notes=notes)

@app.route("/add", methods=["POST"])
def add_note():
    title = request.form.get("title")
    content = request.form.get("content")
    notes.append({
        "id": len(notes) + 1,
        "title": title,
        "content": content
    })
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
