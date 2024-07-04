import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())

from fastapi import FastAPI, Depends
import uvicorn
from uvicorn.config import LOGGING_CONFIG


from routers import user_controller, items_controller


def create_app(): 
    app = FastAPI()
    app.include_router(user_controller.router)
    app.include_router(items_controller.router)
    
    return app

def main():    
    app = create_app()
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    port = int(os.getenv("PORT", 5000))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()



