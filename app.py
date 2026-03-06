from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

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

    response = requests.post(RASA_URL, json=payload)
    bot_response = response.json()

    if bot_response:
        return jsonify({"reply": bot_response[0]["text"]})
    else:
        return jsonify({"reply": "Sorry, I didn't understand that."})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render gives PORT automatically
    app.run(host="0.0.0.0", port=port)