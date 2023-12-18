from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError
from utils import firestore_db

# Change this to HTTPBearer since you're only verifying Firebase tokens
oauth2_scheme = HTTPBearer()

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        token_credentials = token.credentials
        decoded_token = auth.verify_id_token(token_credentials)
        uid = decoded_token['uid']
        return auth.get_user(uid)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )