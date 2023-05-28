from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.countries.controller import router as router_countries
from services.categories.controller import router as router_categories

def get_app() -> FastAPI:
    app: FastAPI = FastAPI()

    # middleware 등록히기
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://127.0.0.1"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE"],
        allow_headers=["*"]
    )

    # services 내의 router 들을 등록하기
    app.include_router(router=router_countries)
    app.include_router(router=router_categories)

    return app
