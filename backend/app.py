from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Endpoint to run Deploy.py
@app.route('/run_deploy', methods=['POST'])
def run_deploy():
    try:
        # Run the Deploy.py script
        subprocess.run(['python3', 'Deploy.py'], check=True)
        return jsonify({'status': 'success', 'message': 'Deploy.py ran successfully.'})
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
