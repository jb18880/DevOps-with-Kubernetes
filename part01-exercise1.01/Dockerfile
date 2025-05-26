FROM python:3.9-slim

#通过添加Dockerfile变量的方式，禁用 Python 的输出缓冲，可以保证输出结果在启动容器后实时刷新
#如果不添加该参数，python只会在缓冲区满的时候才输出信息到屏幕上
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY app.py .
CMD ["python", "app.py"]
