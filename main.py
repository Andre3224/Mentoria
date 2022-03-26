from fastapi import FastAPI

app = FastAPI()

msg = 'OK -- o status code é 200'

@app.get("/")
async def root():
    return {"message": msg}
