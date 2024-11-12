from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models.user import Role
from auth.jwt_handler import verify_token
from db.database import users_collection

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = users_collection.find_one({"email": payload.get("sub")})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

def role_required(role: Role):
    def _role_required(current_user: dict = Depends(get_current_user)):
        if current_user["role"] != role:
            raise HTTPException(status_code=403, detail="Permission denied")
        return current_user
    return _role_required
