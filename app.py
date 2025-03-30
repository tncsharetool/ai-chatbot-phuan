
from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "")
    
    # Example response
    if "tràm" in message.lower():
        reply = (
            "Xin chào Quý khách hàng! Bên chúng tôi có dịch vụ thu mua cây tràm. "
            "Để thuận tiện cho việc báo giá, xin Quý khách vui lòng cung cấp thêm một số thông tin sau:
"
            "1. Số lượng cây tràm muốn bán.
"
            "2. Đường kính và chiều cao tương đối của cây.
"
            "3. Trạng thái sức khỏe của cây: có hiện tượng sâu bệnh hay không.
"
            "Sau khi nhận được thông tin, chúng tôi sẽ kiểm tra và báo giá trong thời gian sớm nhất. "
            "Chân thành BIẾT ƠN!"
        )
    else:
        reply = "Xin chào! Vui lòng cung cấp thêm thông tin để chúng tôi hỗ trợ tốt hơn."
    
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
