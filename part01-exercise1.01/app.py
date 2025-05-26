# 使用官方的 Python 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将应用程序代码复制到容器内
COPY app.py .

# 设置默认命令
CMD ["python", "app.py"]

