from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Global variable to track error state
error_enabled = False

@app.route('/')
def home():
    """Home endpoint that returns basic server information."""
    return jsonify({
        'message': 'Python Sample Server is running!',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/error/enable', methods=['POST'])
def enable_error():
    """Enable error generation on demand."""
    global error_enabled
    error_enabled = True
    logger.info("Error generation enabled")
    return jsonify({
        'message': 'Error generation enabled',
        'status': 'enabled'
    })

@app.route('/error/disable', methods=['POST'])
def disable_error():
    """Disable error generation."""
    global error_enabled
    error_enabled = False
    logger.info("Error generation disabled")
    return jsonify({
        'message': 'Error generation disabled',
        'status': 'disabled'
    })

@app.route('/error/status')
def error_status():
    """Check current error generation status."""
    return jsonify({
        'error_enabled': error_enabled,
        'timestamp': datetime.now().isoformat()
    })

@app.route('/trigger-error')
def trigger_error():
    """Endpoint that generates an error when enabled."""
    global error_enabled
    
    if error_enabled:
        # INTENTIONAL ERROR: This will cause a NameError because 'undefined_variable' is not defined
        # This is the error that can be fixed in a PR
        result = undefined_variable + "This should cause an error"
        return jsonify({'result': result})
    else:
        return jsonify({
            'message': 'Error generation is disabled. Enable it first with POST /error/enable',
            'status': 'disabled'
        })

@app.route('/api/data', methods=['GET'])
def get_data():
    """Sample API endpoint that returns some data."""
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Item 1', 'value': 100},
            {'id': 2, 'name': 'Item 2', 'value': 200},
            {'id': 3, 'name': 'Item 3', 'value': 300}
        ],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/data/<int:item_id>', methods=['GET'])
def get_data_item(item_id):
    """Get a specific data item by ID."""
    data = [
        {'id': 1, 'name': 'Item 1', 'value': 100},
        {'id': 2, 'name': 'Item 2', 'value': 200},
        {'id': 3, 'name': 'Item 3', 'value': 300}
    ]
    
    item = next((item for item in data if item['id'] == item_id), None)
    
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True) 