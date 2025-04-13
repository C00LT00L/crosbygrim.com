from flask import Flask, request, send_from_directory, send_file
import os

app = Flask(__name__, static_folder='static')

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('static', 'index.html')

# Save user input to log.txt
@app.route('/save', methods=['POST'])
def save_input():
    data = request.json
    user_input = data.get('input', '')
    with open('log.txt', 'a') as f:
        f.write(user_input + '\n')
    return '', 200

# View contents of log.txt in browser
@app.route('/log')
def view_log():
    if not os.path.exists('log.txt'):
        return "No log yet."
    with open('log.txt', 'r') as f:
        return f"<pre>{f.read()}</pre>"

# Download log.txt as a file
@app.route('/download')
def download_log():
    if not os.path.exists('log.txt'):
        return "No log yet."
    return send_file('log.txt', as_attachment=True)

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
