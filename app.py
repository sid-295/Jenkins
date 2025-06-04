from flask import Flask, request, jsonify

app = Flask(__name__)
notes = []

@app.route("/")
def index():
    return "Welcome to the Notes App!"

@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def add_note():
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

