from fastapi import FastAPI

app = FastAPI()

msg = 'Olá, isto é um teste em FastAPI'

@app.get("/")
async def root():
    return {"message": msg}
