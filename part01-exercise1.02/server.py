# server.py
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    port = os.getenv('PORT', 5000)  # 获取环境变量 PORT，默认为 5000
    return f"Server started in port {port}!"

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))  # 获取端口
    print(f"Server started in port {port}! Ready to accept requests.")
    app.run(host='0.0.0.0', port=port)  # 启动服务器，监听所有网络接口

