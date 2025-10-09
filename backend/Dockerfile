# 使用官方的 Python 镜像作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制你的 FastAPI 项目代码
COPY . .

# 暴露端口（默认是 8000）
EXPOSE 8000

# 运行 uvicorn 服务器（指向你的 main.py 路径）
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]