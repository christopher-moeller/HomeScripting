from flask import Flask, send_from_directory, jsonify, Response
from frontend import build_frontend
import webbrowser
import os
import rest_service
from api import api

build_frontend()

app = Flask(__name__, static_folder="../frontend/dist")

app.register_blueprint(api, url_prefix="/api")

# Serve React's index.html for all routes except /api/*
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # React's index.html for SPA routing
        return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    webbrowser.open("http://localhost:8080")
    app.run(host="localhost", port=8080)
