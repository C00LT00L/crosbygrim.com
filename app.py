from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_folder='static')

@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

@app.route('/save', methods=['POST'])
def save_input():
    data = request.json
    user_input = data.get('input', '')
    with open('log.txt', 'a') as f:
        f.write(user_input + '\n')
    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
