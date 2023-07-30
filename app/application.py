from flask import Flask, request

from service import detect_sensitive_info, send_prompt

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the prompt from the webhook request
    prompt = request.json['prompt']

    # Detect sensitive information in the prompt using your plugin
    sensitive_info_detected, sensitive_info_messages = detect_sensitive_info(prompt)

    # If no sensitive information is detected, send the prompt to ChatGPT
    if sensitive_info_detected:
        return sensitive_info_messages
    else:
        return send_prompt(prompt)


if __name__ == '__main__':
    app.run()
