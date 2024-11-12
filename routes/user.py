from fastapi import APIRouter, Depends, HTTPException
from auth.oauth import oauth2_scheme
from auth.jwt_handler import verify_token
from db.database import users_collection
from models.user import UserInDB
from auth.dependencies import role_required
from models.user import Role

router = APIRouter()

@router.get("/profile", response_model=dict)
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = users_collection.find_one({"email": payload.get("sub")})
    print(user)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user_data = {
        "username": user.get("username"),
        "email": user.get("email"),
        "id": str(user["_id"])  # Convert MongoDB ObjectId to string
    }
    
    return user_data

@router.get("/", response_model=list[UserInDB])
async def get_all_users(current_user: dict = Depends(role_required(Role.admin))):
    users = list(users_collection.find())
    return users
