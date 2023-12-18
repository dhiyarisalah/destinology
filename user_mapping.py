# USER MAPPING
from firebase_admin.auth import UserRecord
import traceback
from utils import firestore_db
import random

async def get_mapped_user_id(firebase_user: UserRecord) -> int:
    try:
        user_mapping_ref = firestore_db.collection('user_mappings').document(firebase_user.uid)
        doc = await user_mapping_ref.get()
        
        # Check if the user mapping already exists
        if doc.exists:
            return doc.to_dict().get('mapped_user_id')
        else:
            # Assign a random user_id from 1-300 and store the mapping
            assigned_user_id = random.randint(1, 300)
            await user_mapping_ref.set({'mapped_user_id': assigned_user_id})
            return assigned_user_id
    except Exception as e:
        print(f"Error in get_mapped_user_id: {e}")
        traceback.print_exc()
        return None
