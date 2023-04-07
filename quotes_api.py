from fastapi import FastAPI

app = FastAPI()


@app.get('/quotes/random')
async def send_random_quote():
    ...


@app.post('/quotes')
async def create_quote():
    ...
