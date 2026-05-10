from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Jenkins CI/CD Pipeline! 🚀",
        "status": "running",
        "version": "2.0.0",
        "updated": "Auto-deployed via Jenkins webhook!"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/version")
def version():
    return jsonify({
        "version": "2.0.0",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "deployed_by": "Jenkins CI/CD"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
