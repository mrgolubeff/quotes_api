from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.sql.functions import random
from sqlalchemy.orm import Session
from db_models import Base, Quote

app = FastAPI()
db_engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(db_engine)
with Session(db_engine) as session:
    quotes = []
    quotes.append(Quote(author='Vladimir', content='foobar'))
    quotes.append(Quote(author='Dmitry', content='cheburek'))
    quotes.append(Quote(author='Volk', content='helloworld'))
    session.add_all(quotes)
    session.commit()


@app.get('/quotes/random')
async def send_random_quote():
    author = ''
    text = ''
    with Session(db_engine) as session:
        query = select(Quote).group_by(random()).limit(1)
        quote_obj: Quote = session.scalars(query).one()
        author = quote_obj.author
        text = quote_obj.content
    return {'author': author, 'quote': text}


@app.post('/quotes')
async def create_quote():
    ...
