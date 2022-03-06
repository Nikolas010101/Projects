from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    #published é opcional e tem valor padrão

while True:
    try:    
        conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres', password = '29480783', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connection was succesfull!')
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(2)

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
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {'data':posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    #RETORNA O VALOR DA QUERY DO CURSOR
    new_post = cursor.fetchone()
    #COMITAR AS MUDANÇAS NA BASE DE DADOS
    conn.commit()
    return {'data': new_post}


@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    return {'data': updated_post}