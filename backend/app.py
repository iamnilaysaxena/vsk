from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route('/api')
def get_hostname():
    hostname = socket.gethostname()
    return jsonify({"backend_hostname": hostname})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
