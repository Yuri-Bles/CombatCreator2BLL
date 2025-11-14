"""
Module Dockstring.
"""

print("Hello")

from flask_cors import CORS
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from flask import Flask, jsonify, request

from combat_creator_2bll import combat_system_draft
from combat_creator_7tdal import stat_repository

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type", "api-key"])

users = []

API_KEY = "w6+7OT8yc>I=aR%)h{sG(dTU"

@app.route('/combat_system_draft', methods=['OPTIONS'])
def options():
    return jsonify({}), 200

@app.before_request
def require_api_key():
    """
    Method Dockstring.
    """
    if request.method == 'OPTIONS':
        return None

    key = request.headers.get("api-key")
    print(f"API key received: '{key}'")
    print(f"Expected key: '{API_KEY}'")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    print("Succeeded API key check")
    return None

@app.route('/combat_system_draft', methods=['POST'])
def add_stat():
    """
    Method Dockstring.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    required = ["name", "default_value", "min_value", "max_value"]
    if not all(key in data for key in required):
        return jsonify({"error": f"Missing one of: {', '.join(required)}"}), 400

    try:
        combat_system_draft.CombatSystemDraft(
            stat_repository, "Test System"
        ).add_stat(
            data["name"],
            float(data["default_value"]),
            float(data["min_value"]),
            float(data["max_value"]),
        )
        return jsonify({"message": "Stat created successfully"}), 201

    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/combat_system_draft', methods=['GET'])
def get_all_stats():
    """
    Method Dockstring.
    """
    print("Hit stat method")
    try:
        _stats = combat_system_draft.CombatSystemDraft().get_all_stats()
        print("Hit return")
        return jsonify({
            "message": "Stats successfully retrieved",
            "stats": _stats
        }), 200
    except Exception as e:
        return jsonify({"error": "Failed to get stats", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
