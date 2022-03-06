from typing import Optional
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #published é opcional e tem valor padrão
    rating: Optional[int] = None
    #rating é opcional e não tem valor padrão

#decorator passa a função como parâmetro para o método do objeto

@app.get('/')
def root():
    return {'message':'Hello World'}

@app.get('/posts')
def get_posts():
    return {'data':'These are your posts'}

@app.post('/createposts')
def create_posts(post: Post):
    print(post)
    print(post.title)
    print(post.dict())
    return {'data': post}