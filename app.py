from flask import Flask, render_template, url_for, request, jsonify
import requests, json

app = Flask(__name__)

@app.route('/',methods=["POST", "GET"])
def chat():
    text=str(request.form.get('text'))
    payload = json.dumps({"sender": "Rasa","message": text})
    response = requests.request("POST",   url="http://localhost:5005/webhooks/rest/webhook", data=payload)
    response=response.json()
    return jsonify({"status":"success","response":response})

if __name__ == "__main__":
    app.run(debug = True, port = 5000)