import os
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
from fastapi import FastAPI, Depends
import uvicorn
from uvicorn.config import LOGGING_CONFIG
from fastapi.middleware.cors import CORSMiddleware


from routers import (user_controller, items_controller, cart_controller,
                     report_controller, payment_controller)


def create_app(): 
    app = FastAPI()
    app.include_router(user_controller.router)
    app.include_router(items_controller.router)
    app.include_router(cart_controller.router)
    app.include_router(payment_controller.router)
    app.include_router(report_controller.router)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000"],  # React's URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app

def main():    
    app = create_app()
    LOGGING_CONFIG["formatters"]["default"]["fmt"] = "%(asctime)s [%(name)s] %(levelprefix)s %(message)s"
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()



