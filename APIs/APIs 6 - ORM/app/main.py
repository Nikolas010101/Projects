from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

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

@app.get('/')
def root():
    return {'message':'Hello World'}


@app.get('/posts')
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")
    # posts = cursor.fetchall()
    
    posts = db.query(models.Post).all()
    return {'data':posts}


@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",(post.title, post.content, post.published))
    # #RETORNA O VALOR DA QUERY DO CURSOR
    # new_post = cursor.fetchone()
    # #COMITAR AS MUDANÇAS NA BASE DE DADOS
    # conn.commit()
    
    #podemos adicionar cada entrada manualmente, ou podemos dar unpack no modelo do pydantic
    
    # new_post = models.Post(title = post.title, content = post.content, published = post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    #refresh age como um RETURNING *
    db.refresh(new_post)
    return {'data': new_post}


@app.get('/posts/{id}')
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
    # post = cursor.fetchone()
    
    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    return {"post_detail": post}


@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    
    post.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    updated_post = post_query.first()
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post with id: {id} was not found')
    post_query.update(post.dict(), synchronize_session=False)
    
    db.commit()
    
    return {'data': post_query.first()}