from flask import jsonify
from flask import request

from app import app
from app.utils.image_text import detect_text
from app.utils.audio_text import transcribe_text


@app.route('/handle_file', methods=['POST'])
def handle_file():
    if request.method == 'POST':
        file = request.files['text']
        if '.jpg' in file.filename or '.png' in file.filename:
            result = detect_text(file)
        elif '.mp3' in file.filename or '.wav' in file.filename:
            result = transcribe_text(file)

        return jsonify({
            'result':  result
        })
