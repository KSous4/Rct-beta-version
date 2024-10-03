from ultralytics import YOLO
from copy import deepcopy
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Classifier:
    def __init__(self):
        pass

    model = YOLO('/app/services/yolov10x.pt')

    classes_parse = {
        2.0: 1,
        3.0: 9,
        5.0: 2,
        7.0: 2
    }

    @staticmethod
    def classify(img):
        try:
            results = Classifier.model(img, imgsz=640, max_det=2, classes=[2, 3, 5, 7], verbose=False)
            num_detections = len(results[0].boxes.xyxy) if results[0].boxes.xyxy is not None else 0
            if num_detections > 0:
                results = Classifier.get_leftmost(results)

            return {
                "results": {
                    "class": Classifier.classes_parse.get(results[0].boxes.cls[0].item()),
                    "conf": round(results[0].boxes.conf[0].item(), 2)
                }
            }

        except:
            return {
                "results": {
                    "class": "Veiculo não classificado",
                    "conf": 999.0
                }
            }

    @staticmethod
    def get_leftmost(results):
        xmin_values = [box[0].item() for box in results[0].boxes.xyxy]
        min_xmin_index = xmin_values.index(min(xmin_values))
        leftmost_results = deepcopy(results[0])
        leftmost_results.boxes = leftmost_results.boxes[min_xmin_index:min_xmin_index + 1]
        return leftmost_results
