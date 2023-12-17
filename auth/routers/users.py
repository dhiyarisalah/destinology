from fastapi import APIRouter, Request
from fastapi import APIRouter, Depends, HTTPException, status

from dependencies import get_current_user

from schemas.users import UserSchema
from schemas.auth import PasswordResetSchema
from fastapi.responses import JSONResponse
from utils import firestore_db, ExceptionResponse
from firebase_admin import auth
from utils import user_exists

router = APIRouter()


# Get User Profile
@router.get("/me")
async def get_user(current_user: auth.UserRecord = Depends(get_current_user)):
    try:
        user_doc_ref = firestore_db.collection("users").document(current_user.uid)
        user_doc = await user_doc_ref.get()  # Use 'await' to get the document
        return user_doc.to_dict() if user_doc.exists else {"message": "User not found"}
    except Exception as e:
        return ExceptionResponse(e)


@router.put("/me")
async def update_user(updated_user: UserSchema, current_user: auth.UserRecord = Depends(get_current_user)):
    try:
        # Update Firebase Auth User
        auth.update_user(
            current_user.uid,
            email=updated_user.email,
            display_name=updated_user.full_name
        )
        # Update Firestore User Document
        user_doc_ref = firestore_db.collection("users").document(current_user.uid)
        await user_doc_ref.set({
            "email": updated_user.email,
            "username": updated_user.username,
            "full_name": updated_user.full_name
        }, merge=True)
        user_doc = await user_doc_ref.get()  # Use 'await' to get the document
        return user_doc.to_dict()
    except Exception as e:
        return ExceptionResponse(e)


@router.delete("/me")
async def delete_user(current_user: auth.UserRecord = Depends(get_current_user)):
    try:
        user_doc_ref = firestore_db.collection("users").document(current_user.uid)
        
        # Asynchronous deletion of the Firestore document
        await user_doc_ref.delete()

        # Delete the user from Firebase Auth
        auth.delete_user(current_user.uid)

        return {"message": "User deleted successfully"}
    except Exception as e:
        # Log the exception for debugging
        print(f"Error in deleting user: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# @router.post("/me/password-reset")
# async def reset_password(password_reset: PasswordResetSchema, current_user: auth.UserRecord = Depends(get_current_user)):
#     try:
#         auth.update_user(current_user.uid, password=password_reset.new_password)
#         return {"message": "Password updated successfully"}
#     except Exception as e:
#         return ExceptionResponse(e)
