"""
Module Dockstring.
"""

from flask_cors import CORS
import sys
import os
import traceback

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from flask import Flask, jsonify, request

from combat_creator_2bll import combat_system_draft
from combat_creator_4dal.database import get_session
from combat_creator_4dal.stat_repository import StatRepository

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type", "api-key"])

stat_repository = StatRepository()
combat_system = combat_system_draft.CombatSystemDraft(stat_repository, "Test System")

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
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401
    return None

@app.route('/create_system_stat', methods=['POST'])
def create_system_stat():
    try:
        data = request.get_json()

        system_id = data.get("system_id")

        if system_id is None:
            return jsonify({"error": "system_id is required"}), 400

        with get_session() as session:
            result = combat_system.create_system_stat(system_id, session)

        return jsonify({"message": "Stat created", "result": result}), 200
    
    except Exception as e:
        print("SERVER ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/combat_system_draft', methods=['GET'])
def get_all_stats():
    """
    Method Dockstring.
    """
    try:
        with get_session() as session:
            system_id = request.args.get("system_id", type=int)
            _stats = combat_system.get_stats_by_system_id(system_id, session)
        return jsonify({
            "message": "Stats successfully retrieved",
            "stats": _stats
        }), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Failed to get stats", "details": str(e)}), 500

@app.route('/update_system_stats_by_system_id', methods=['POST'])
def update_system_stats_by_system_id():
    try:
        data = request.get_json()

        system_id = data.get("system_id")
        stats = data.get("stats")

        if system_id is None:
            return jsonify({"error": "system_id is required"}), 400
        
        if stats is None:
            return jsonify({"error": "stats are required"}), 400

        with get_session() as session:
            result = combat_system.update_system_stats_by_system_id(system_id, session, stats)

        return jsonify({"message": "Stats updated", "result": result}), 200
    
    except Exception as e:
        print("SERVER ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@app.route('/delete_system_stat', methods=['POST'])
def delete_system_stat():
    try:
        data = request.get_json()

        stat_id = data.get("stat_id")

        if stat_id is None:
            return jsonify({"error": "stat_id is required"}), 400

        with get_session() as session:
            combat_system.delete_system_stat(stat_id, session)

        return jsonify({"message": "Stat deleted"}), 200
    
    except Exception as e:
        print("SERVER ERROR:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
