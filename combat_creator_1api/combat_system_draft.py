from flask import Flask, jsonify
from combat_creator_2bll.combat_system_draft import CombatSystemDraft
from combat_creator_4dal.database import get_session

app = Flask(__name__)

@app.route('/combat_system_draft', methods=['GET'])
def GetStats():
    combat_system_draft = CombatSystemDraft()
    with get_session() as session:
        stats = combat_system_draft.get_stats_by_system_id(session)

    if (stats):
        return jsonify(message="Stats succesfully retrieved", stats=stats), 200
    else:
        return jsonify(message="Failed to get stats"), 500

if __name__ == '__main__':
    app.run(debug=True)