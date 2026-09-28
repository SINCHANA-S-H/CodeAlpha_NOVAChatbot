from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({
        "status": "online",
        "assistant": "NOVA"
    })


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message", "")

    from chatbot import process_message

    response = process_message(message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)