from fastapi import FastAPI
from src.api import produt_api
app = FastAPI(description = "API for verify INTELLIGENCE STOCK")

app.include_router(produt_api.product_router,tags = ["Product Tag"])