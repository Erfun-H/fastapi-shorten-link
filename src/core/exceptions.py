from fastapi import HTTPException

class CustomHTTPException(HTTPException):
    def __init__(self, status_code, message: str = "", details = None, headers = None):
        self.message = message
        self.details = details
        super().__init__(status_code, headers)
