from fastapi import FastAPI

app = FastAPI()


@app.get('/quotes/random')
async def send_random_quote():
    ...
