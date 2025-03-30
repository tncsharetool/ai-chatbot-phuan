from flask import Flask, render_template, request, jsonify
import openai, os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

def load_prompt():
    try:
        with open("bot_prompt_phuan_mua_cay_rung_dam_go.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Prompt mặc định"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=load_prompt() + "\nUser: " + message + "\nBot:",
            max_tokens=300,
            temperature=0.7
        )
        reply = response["choices"][0]["text"].strip()
    except Exception as e:
        reply = f"Lỗi: {str(e)}"
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
