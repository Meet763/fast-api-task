from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserCreate, UserInDB, Token
from auth.jwt_handler import create_access_token
from utils.hashing import hash_password, verify_password
from db.database import users_collection

router = APIRouter()

@router.post("/signup", response_model=dict)
async def signup(user: UserCreate):
    
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_in_db = UserInDB(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    users_collection.insert_one(user_in_db.__dict__)
    access_token = create_access_token({"sub": user_in_db.email})
    
    return {"message": "User created successfully", "token": access_token}

@router.post("/login", response_model=Token)
async def login(user: UserCreate):

    
    user_data = users_collection.find_one({"email": user.email})
    
    if not user_data or not verify_password(user.password, user_data["hashed_password"]):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    access_token = create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
