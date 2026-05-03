from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
frontend_dir = os.path.join(current_dir, 'frontend')

sys.path.insert(0, current_dir)

from password_checker import check_password_strength, load_common_passwords, check_against_common
from password_generator import generate_password

app = Flask(__name__)
CORS(app)

common_passwords = load_common_passwords()

@app.route("/")
def home():
    return send_from_directory(frontend_dir, 'index.html')

@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(frontend_dir, filename)

@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.json
        password = data.get("password", "")
        if not password:
            return jsonify({"error": "Password required"}), 400
        strength, score, feedback = check_password_strength(password)
        is_unique, common_msg = check_against_common(password, common_passwords)
        return jsonify({
            "strength": strength,
            "score": score,
            "feedback": feedback,
            "common_check": common_msg,
            "is_unique": is_unique
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/generate", methods=["POST", "GET"])
def generate():
    try:
        length = 16
        if request.method == "POST" and request.json:
            length = request.json.get("length", 16)
        password = generate_password(length)
        strength, score, feedback = check_password_strength(password)
        return jsonify({
            "password": password,
            "strength": strength,
            "score": score
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("="*60)
    print("PASSWORD SECURITY TOOL")
    print("Open: http://127.0.0.1:5000")
    print("="*60)
    app.run(debug=True, port=5000, host='127.0.0.1')