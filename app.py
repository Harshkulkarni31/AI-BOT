
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json['text'].lower()
    if "your name" in user_input:
        response = "my name is  Bot AI."
    else:
        response = "Im learning"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
