from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:29480783@localhost/fastapi'

#engine é o que conecta o sqlalchemy a uma base de dados do postgres

engine = create_engine(SQLALCHEMY_DATABASE_URL)

#para a comunicação de fato precisamos declarar uma sessão

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#modelos das tabelas serão definidos com base na classe Base
Base = declarative_base()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()