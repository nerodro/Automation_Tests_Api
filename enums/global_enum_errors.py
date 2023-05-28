from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Statuse code isn't equal to expected"
    WRONG_JSON_DATA = "Data in json respons not equal to expected"