# Dockerfile

# 使用官方的Python镜像作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制应用代码
COPY . /app

# 安装应用所需的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露容器监听的端口
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py

# 在容器启动时运行应用
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]



