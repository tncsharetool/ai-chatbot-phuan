from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_bot_prompt():
    try:
        with open("bot_prompt_phuan_mua_cay_rung_dam_go.txt", "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Bạn là nhân viên tư vấn chuyên nghiệp về thu mua cây trồng."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": load_bot_prompt()},
            {"role": "user", "content": message}
        ]
    )
    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
