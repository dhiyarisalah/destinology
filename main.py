# MAIN
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, users, iteniary
from dependencies import get_current_user
from routers.iteniary import router as iteniary_router
from routers.Landmark import router as landmark_router

app = FastAPI(title="Destinology", description="Itinerary Planner API")

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
    tags=["Authentication"],
    responses={404: {"description": "Not found"}}
)
app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)],
)

app.include_router(
    iteniary_router,
    prefix="/models",
    tags=["Itinerary Planner"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)]
)

app.include_router(
    landmark_router,
    prefix="/models",
    tags=["Landmark Prediction"],
    responses={404: {"description": "Not found"}}
)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
