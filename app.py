from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Lấy API Key từ biến môi trường
openai.api_key = os.getenv("OPENAI_API_KEY")

# Đọc prompt huấn luyện từ file
def load_prompt():
    try:
        with open("bot_prompt_phuan_mua_cay_rung_dam_go.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Bạn là nhân viên tư vấn thu mua cây rừng chuyên nghiệp."

# Giao diện chính
@app.route('/')
def home():
    return render_template("index.html")

# API Chat
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get("message", "")

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": load_prompt()},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": f"Lỗi: {str(e)}"}), 500

# Khởi chạy app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
