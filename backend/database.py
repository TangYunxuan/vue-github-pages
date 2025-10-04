from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 建议统一使用这个变量作为你的数据库文件名
sqlite_file_name = "tangyunxuan.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///./{sqlite_file_name}"

# 创建数据库引擎
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 创建 Session 类，用于生成数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建 Base 类，供模型继承
Base = declarative_base()

# 每次请求中获取数据库 session（FastAPI 推荐做法）
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()