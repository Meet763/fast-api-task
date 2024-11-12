from fastapi import FastAPI
from routes import auth, user

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "welcome to fast api task"}

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])



