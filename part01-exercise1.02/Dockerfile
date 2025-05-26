FROM python:3.9-slim
WORKDIR /app
COPY server.py /app/
#安装Flask库
RUN pip install flask
#设置环境变量（默认端口为5000）
ENV PORT=5000
#启动Flask
CMD ["python","server.py"]
