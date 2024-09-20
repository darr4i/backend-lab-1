from . import app

from flask import jsonify
from datetime import datetime

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({
        'status': 'OK',
        'timestamp': datetime.utcnow().isoformat()
    }), 200
