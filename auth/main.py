import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users
from dependencies import get_current_user

app = FastAPI(title="Destinology", description="Authentication API")

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],  # Adjust in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}}
)
app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)],
)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
