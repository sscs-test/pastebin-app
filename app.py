from flask import Flask, request, jsonify
from flask_httpauth import HTTPTokenAuth
import uuid
import platform
import subprocess
import sys

app = Flask(__name__)
auth = HTTPTokenAuth(scheme='Bearer')

# In-memory storage for users and their API keys and notes
tokens = {}
notes_by_user = {}

# Function to generate a new API key
def generate_api_key():
    return str(uuid.uuid4())

def cmd(args):
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    out, _ = process.communicate()
    return out.decode('ascii').strip()

@app.route('/')
def python_versions():
    bazel_python_path = f'Python executable used by Bazel is: {sys.executable} <br/><br/>'
    bazel_python_version = f'Python version used by Bazel is: {platform.python_version()} <br/><br/>'
    host_python_path = f'Python executable on the HOST machine is: {cmd(["which", "python3"])} <br/><br/>'
    host_python_version = f'Python version on the HOST machine is: {cmd(["python3", "-c", "import platform; print(platform.python_version())"])}'
    python_string = (
        bazel_python_path
        + bazel_python_version
        + host_python_path
        + host_python_version
    )
    return python_string

# API for user signup and API key generation
@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if username in tokens.values():
        return jsonify({"error": "Username already exists"}), 400
    
    api_key = generate_api_key()
    tokens[api_key] = username
    notes_by_user[username] = []  # Initialize an empty notes list for the new user
    
    return jsonify({"message": "User registered successfully", "api_key": api_key}), 201

# Authentication function
@auth.verify_token
def verify_token(token):
    bearer = request.headers.get('Authorization')
    token = bearer.split()[1]
    if token in tokens:
        return tokens[token]
    return None

# API to add new note (requires valid API key)
@app.route('/add_note', methods=['POST'])
@auth.login_required
def add_note():
    data = request.get_json()
    note = data.get('note')
    
    if not note:
        return jsonify({"error": "Note content is required"}), 400
    
    # Get the username from the apikey
    username = auth.current_user()
    notes_by_user[username].append(note)
    
    return jsonify({"message": "Note added successfully"}), 201

# API to read all notes (requires valid API key)
@app.route('/notes', methods=['GET'])
@auth.login_required
def get_notes():
    # Get the username from the apikey
    username = auth.current_user()
    
    # Fetch notes specific to the user
    user_notes = notes_by_user.get(username, [])
    
    return jsonify({"notes": user_notes}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

