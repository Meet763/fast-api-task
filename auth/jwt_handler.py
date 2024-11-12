# utils.py
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
import os
from dotenv import load_dotenv


SECRET_KEY = str(os.getenv("SECRET_KEY"))
ALGORITHM =  str(os.getenv("ALGORITHM"))
ACCESS_TOKEN_EXPIRE_MINUTES =  120

def create_access_token(data: dict):
    
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    print(SECRET_KEY)
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except JWTError:
        return None
