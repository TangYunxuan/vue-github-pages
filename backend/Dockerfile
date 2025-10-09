# 使用官方的 Python 镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 复制 requirements.txt 文件
COPY backend/requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制 FastAPI 项目代码
COPY backend/ .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]