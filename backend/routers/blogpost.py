from fastapi import APIRouter
from crud.blogpost import list_blogposts

router = APIRouter(prefix="/api/blogposts", tags=["BlogPosts"])

@router.get("/")
def get_blogposts():
    return list_blogposts()