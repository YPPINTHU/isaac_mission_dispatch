from .cors_config import CORSConfig

def main():
    parser = argparse.ArgumentParser()
    # ...existing arguments...
    
    # Enhanced CORS-related arguments
    parser.add_argument("--cors_origins", nargs="*", 
                       help="List of allowed origins for CORS (e.g., http://localhost:8080)")
    parser.add_argument("--cors_methods", nargs="*",
                       help="List of allowed HTTP methods for CORS") 
    parser.add_argument("--cors_headers", nargs="*",
                       help="List of allowed headers for CORS")
    parser.add_argument("--disable_cors_credentials", action="store_true",
                       help="Disable credentials for CORS")
    parser.add_argument("--cors_max_age", type=int, default=600,
                       help="Max age for CORS preflight requests in seconds")

    args = parser.parse_args()

    # Create CORS config from arguments
    cors_config = CORSConfig(
        allowed_origins=args.cors_origins,
        allowed_methods=args.cors_methods,
        allowed_headers=args.cors_headers,
        allow_credentials=not args.disable_cors_credentials,
        max_age=args.cors_max_age
    )

    # Create and start server with CORS config
    server = WebServer(host=args.address, port=args.port,
                      controller_port=args.controller_port,
                      cors_config=cors_config)
    server.run()