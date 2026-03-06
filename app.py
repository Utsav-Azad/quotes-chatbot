from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Rasa server inside same container
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/send", methods=["POST"])
def send_message():
    user_message = request.json["message"]

    payload = {
        "sender": "user",
        "message": user_message
    }

    try:
        response = requests.post(RASA_URL, json=payload, timeout=15)
        response.raise_for_status()

        bot_response = response.json()

        if bot_response:
            return jsonify({"reply": bot_response[0].get("text", "No reply")})
        else:
            return jsonify({"reply": "Sorry, I didn't understand that."})

    except Exception as e:
        print("Error connecting to Rasa:", e)
        return jsonify({"reply": "Bot is temporarily unavailable."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)