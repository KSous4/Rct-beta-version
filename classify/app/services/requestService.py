from fastapi import UploadFile, HTTPException
import numpy as np
import cv2 as cv

from app.services.classify import Classifier

class ReqService:


    @staticmethod
    async def request_handler(file: UploadFile):
        try:

            image_data = await file.read()

            nparr = np.frombuffer(image_data, np.uint8)

            img = cv.imdecode(nparr, cv.IMREAD_COLOR)

            if img is None:
                raise HTTPException(status_code=400, detail="Invalid image format")

            results = Classifier.classify(img)

            return results

        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
