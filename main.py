from fastapi import FastAPI
from routes import auth, user
import os
import uvicorn

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(user.router, prefix="/users", tags=["Users"])


if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 for local development
    uvicorn.run(app, host="0.0.0.0", port=port)
