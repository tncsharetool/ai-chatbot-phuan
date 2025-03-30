from flask import Flask, render_template, request, jsonify
import openai, os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt():
    with open("bot_prompt_phuan_mua_cay_rung_dam_go.txt", "r", encoding="utf-8") as f:
        return f.read()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": load_prompt()},
            {"role": "user", "content": message}
        ]
    )
    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})
