from flask import Flask, jsonify
from combat_creator_2bll.combat_system_draft import CombatSystemDraft

app = Flask(__name__)

@app.route('/combat_system_draft', methods=['GET'])
def GetAllStats():
    combat_system_draft = CombatSystemDraft()
    stats = combat_system_draft.get_all_stats()
    if (stats):
        return jsonify(message="Stats succesfully retrieved", stats=stats), 200
    else:
        return jsonify(message="Failed to get stats"), 500

if __name__ == '__main__':
    app.run(debug=True)