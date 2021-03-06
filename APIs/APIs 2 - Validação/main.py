from typing import Optional
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #published é opcional e tem valor padrão
    rating: Optional[int] = None
    #rating é opcional e não tem valor padrão

#decorator passa a função como parâmetro para o método do objeto

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p

my_posts = [{"title": "title of post 1", "content":"content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

@app.get('/')
def root():
    return {'message':'Hello World'}

@app.get('/posts')
def get_posts():
    return {'data':my_posts}

@app.post('/posts')
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,9999999)
    my_posts.append(post_dict)
    return {'data': post_dict}

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    return {"post_detail": post}