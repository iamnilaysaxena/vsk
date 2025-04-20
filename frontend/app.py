from flask import Flask, render_template
import socket
import requests

app = Flask(__name__)

# Update this with your actual backend API endpoint later
BACKEND_API_URL = "http://<BE_VMSS_IP>/api"

@app.route("/")
def home():
    fe_hostname = socket.gethostname()

    try:
        response = requests.get(BACKEND_API_URL, timeout=2)
        be_hostname = response.json().get("backend_hostname", "Unavailable")
    except Exception as e:
        be_hostname = "Unavailable"

    return render_template("index.html", fe_hostname=fe_hostname, be_hostname=be_hostname)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
