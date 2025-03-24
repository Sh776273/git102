from flask import Flask, jsonify, request

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Flask API!'})

# Simple API route
@app.route('/api', methods=['GET'])
def api():
    return jsonify({'data': 'API is working!'})

# Route with parameters
@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    return jsonify({'user': username, 'status': 'active'})

# Route with query parameters
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    return jsonify({'query': query, 'result': f'Search result for {query}'})

# POST route with JSON body
@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    return jsonify({'message': 'Data added successfully', 'data': data})

# Error handler for 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not Found'}), 404

