from flask import Flask, send_from_directory, jsonify
from frontend import build_frontend
import webbrowser
import os

build_frontend()

app = Flask(__name__, static_folder="../frontend/dist")

# Serve React's index.html for all routes except /api/*
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # React's index.html for SPA routing
        return send_from_directory(app.static_folder, "index.html")

# Example API route
@app.route("/api/hello")
def api_hello():
    return jsonify({"message": "Hello from Flask API!"})

if __name__ == "__main__":
    webbrowser.open("http://localhost:8080")
    app.run(host="localhost", port=8080)
