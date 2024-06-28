from fastapi import FastAPI
import os
from uvicorn.config import LOGGING_CONFIG
import uvicorn
from sqlalchemy.orm import session

from routers import book_controller, user_controller
from database import engine, SessionLocal
def create_app(): 
    app = FastAPI()
    app.include_router(book_controller.router)
    app.include_router(user_controller.router)
    return app
def main():  
    app = create_app()  
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()


