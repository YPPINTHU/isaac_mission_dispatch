from typing import List, Optional

class CORSConfig:
    """Configuration for CORS settings"""
    def __init__(self,
                 allowed_origins: Optional[List[str]] = None,
                 allowed_methods: Optional[List[str]] = None,
                 allowed_headers: Optional[List[str]] = None,
                 allow_credentials: bool = True,
                 max_age: int = 600):
        
        # Default origins - include common development servers
        self.allowed_origins = allowed_origins or [
            "http://localhost:8080",    # Vite default
            "http://localhost:3000",    # React default
            "http://127.0.0.1:8080",
            "http://127.0.0.1:3000"
        ]
        
        # Default methods - include all common HTTP methods
        self.allowed_methods = allowed_methods or [
            "GET",
            "POST", 
            "PUT",
            "DELETE",
            "PATCH",
            "OPTIONS"
        ]
        
        # Default headers - include commonly needed headers
        self.allowed_headers = allowed_headers or [
            "Content-Type",
            "Authorization", 
            "X-Requested-With",
            "Accept",
            "Origin",
            "Access-Control-Request-Method",
            "Access-Control-Request-Headers"
        ]
        
        self.allow_credentials = allow_credentials
        self.max_age = max_age  # Cache preflight requests