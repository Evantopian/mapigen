from typing import Optional, Any

class MapiError(Exception):
    def __init__(self, message: str, service: Optional[str] = None, operation: Optional[str] = None):
        super().__init__(message)
        self.service = service
        self.operation = operation

class ServiceNotFoundError(MapiError):
    pass

class OperationNotFoundError(MapiError):
    pass

class ValidationError(MapiError):
    pass

class RequestError(MapiError):
    def __init__(self, message: str, error_type: Optional[str] = None, 
                 error_category: Optional[str] = None, http_status: Optional[int] = None, **kwargs: Any):
        super().__init__(message, **kwargs)
        self.error_type = error_type
        self.error_category = error_category  
        self.http_status = http_status
