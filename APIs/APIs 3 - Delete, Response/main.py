from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
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
        
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i

my_posts = [{"title": "title of post 1", "content":"content of post 1", "id": 1}, {"title": "favorite foods", "content": "I like pizza", "id": 2}]

@app.get('/')
def root():
    return {'message':'Hello World'}

@app.get('/posts')
def get_posts():
    return {'data':my_posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,9999999)
    my_posts.append(post_dict)
    return {'data': post_dict}

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    return {"post_detail": post}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)