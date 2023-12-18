from fastapi import APIRouter, HTTPException, Depends
from schemas.iteniary import IteniaryRequest, IteniaryResponse, IteniaryItem
from iteniary_planner import iteniary_planner  # Import the function
from dependencies import get_current_user
from firebase_admin.auth import UserRecord
import traceback
from user_mapping import get_mapped_user_id

router = APIRouter()

@router.post("/iteniary", response_model=IteniaryResponse)
async def create_iteniary(request: IteniaryRequest, firebase_user: UserRecord = Depends(get_current_user)):
    try:
        mapped_user_id = await get_mapped_user_id(firebase_user)
        if not mapped_user_id:
            raise HTTPException(status_code=404, detail="User not found in mapping.")
        
        final_iteniary = iteniary_planner(mapped_user_id, request.city, request.n_days, request.max_budget)
        
        if final_iteniary.empty:
            return IteniaryResponse(itinerary=[])
        
        itinerary_items = [IteniaryItem(place_name=row['place_name'],
                                        price=row['price'],
                                        category=row['category'],
                                        rating=row['rating'],
                                        day=row['day'])
                           for index, row in final_iteniary.iterrows()]
        
        return IteniaryResponse(itinerary=itinerary_items)
    except Exception as e:
        print(f"Error in create_iteniary: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))
