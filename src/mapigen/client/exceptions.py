from typing import Optional

class MapiError(Exception):
    def __init__(self, message: str, service: Optional[str] = None, operation: Optional[str] = None, error_type: str = "unknown", original_exception: Optional[Exception] = None):
        super().__init__(message)
        self.service = service
        self.operation = operation
        self.error_type = error_type
        self.original_exception = original_exception
