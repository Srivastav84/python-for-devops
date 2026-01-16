# Application Entry Point
from app.api import app
import uvicorn

if __name__ == "__main__":
    # ASGI Web Server
    uvicorn.run(
        "app.api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
# http://127.0.0.1:8000/
# http://localhost:8000/
# http://localhost:8000/docs