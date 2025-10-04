from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import blogpost, catphoto, comment, project, traveltrip, user

# 创建数据库表（仅首次运行时会创建）
Base.metadata.create_all(bind=engine)

# 初始化 FastAPI 应用
app = FastAPI(
    title="TangYunxuan Backend",
    description="FastAPI backend for tangyunxuan.com",
    version="1.0.0"
)

# 配置 CORS 中间件（允许前端跨域访问）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 开发阶段允许全部来源，生产环境建议指定域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册各个子模块的路由
app.include_router(blogpost.router, prefix="/api/blogposts", tags=["BlogPost"])
app.include_router(catphoto.router, prefix="/api/catphotos", tags=["CatPhoto"])
app.include_router(comment.router, prefix="/api/comments", tags=["Comment"])
app.include_router(project.router, prefix="/api/projects", tags=["Project"])
app.include_router(traveltrip.router, prefix="/api/traveltrips", tags=["TravelTrip"])
app.include_router(user.router, prefix="/api/users", tags=["User"])

# 根路径测试
@app.get("/")
def root():
    return {"message": "Backend running!"}