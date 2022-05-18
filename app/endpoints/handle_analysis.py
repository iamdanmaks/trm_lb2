from flask import jsonify
from flask import request

from app import app
from app.utils.analyze_text import sample_analyze_entities


@app.route('/handle_analysis', methods=['POST'])
def handle_analysis():
    if request.method == 'POST':
        return jsonify(sample_analyze_entities(request.get_json()['text']))
