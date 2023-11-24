from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html")

from chatgpt import get_response
@app.post("/predict")
def predict():
    chat_history=[]
    text = request.get_json().get("message")
    # TODO: check if text is valid
    response = get_response(text,chat_history)
    chat_history.append((text, response))
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)