from fastapi import FastAPI
from github_routes import router

app = FastAPI(title="BLAES GitHub Access")

app.include_router(router)