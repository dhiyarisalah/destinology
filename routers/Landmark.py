from fastapi import APIRouter, HTTPException, File, UploadFile
from schemas.landmark import LandmarkResponse, LandmarkItem
from PIL import Image
from keras.models import load_model
import io
import traceback
import numpy as np
import json

router = APIRouter()

@router.post("/landmark", response_model=LandmarkResponse)
async def create_landmark(file: UploadFile = File(...)):


    model = load_model("../Model/Landmark-R.h5")
    labels = ["Candi-Borobudur", "Gedung-Sate", "Patung-GWK", "Suro-Boyo", "Tugu-Jogja", "Tugu-Monas"]

    try:
        
        contents = await file.read()
        img = Image.open(io.BytesIO(contents))
        image = img.resize((224, 224))
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)
        highest_score_index = np.argmax(prediction)
        highest_score_label = labels[highest_score_index]

        f_deskripsi = open('../Model/dataset/deskripsi_tempat.json')
        f_fun_fact = open('../Model/dataset/fun_fact_tempat.json')

        desc = json.load(f_deskripsi)
        fun_fact = json.load(f_fun_fact)


        prediction_result = LandmarkItem(name=highest_score_label,
                                        desc=desc[highest_score_label],
                                        fact=fun_fact[highest_score_label])
        
        return LandmarkResponse(landmark=prediction_result)
    

    except Exception as e:
        print(f"Error in recognizing landmark: {e}")
        traceback.print_exc()
        raise HTTPException(status_code=400, detail=str(e))


