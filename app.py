import json
import os
import base64
from flask_cors import CORS
from flask import Flask, render_template, request
from engine import openai_process_message

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
directory = os.path.dirname(os.path.realpath(__file__))


@app.route("/", methods=['GET'])
def hello_world():
    return render_template('home.html')


@app.route('/process-message', methods=['POST'])
def process_message_route():
    # Get user's message and preferred voice from the request
    user_message = request.json.get('userMessage', '')

    print('user_message:', user_message)

    # Call openai_process_message function to process the user's message and get a response
    openai_response_text = openai_process_message(user_message)

    # Clean the response to remove any empty lines
    openai_response_text = os.linesep.join(
        line for line in openai_response_text.splitlines() if line)

    # Send a JSON response back to the user containing the message's response in text format
    response_data = {"openaiResponseText": openai_response_text}
    response = app.response_class(
        response=json.dumps(response_data),
        status=200,
        mimetype='application/json'
    )

    print(response)
    return response


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
