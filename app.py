from flask import Flask, render_template, request, jsonify
import base64
import numpy as np
import cv2

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        img_base64 = data["image"].split(",")[1]

        # Decode base64 to bytes
        img_bytes = base64.b64decode(img_base64)

        # Convert bytes into OpenCV image
        nparr = np.frombuffer(img_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Example detection logic — **replace with your model call**
        # For now we simulate:
        damage_pct = round(np.random.uniform(1, 40), 2)
        status = "Bridge detected"
        life = f"{np.random.randint(5, 25)} years"

        return jsonify({
            "status": status,
            "damage_pct": str(damage_pct),
            "life": str(life)
        })

    except Exception as e:
        print("Analyze error:", e)
        return jsonify({"error": "analysis_failed"}), 500

if __name__ == "__main__":
    app.run(debug=True)




