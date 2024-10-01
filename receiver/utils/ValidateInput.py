from pydantic import ValidationError
from receiver.models.ReviewTransitModel import Ns2ReviewTransit

class ValidateInput:
    def __init__(self):
        pass

    @staticmethod
    def validate_cm_req_body(data: dict):

        root = data.get('soap:Envelope').get('soap:Body').get('ns2:ReviewTransit')
        try:
            Ns2ReviewTransit.model_validate(root)
            return root
        except ValidationError:
            pass


