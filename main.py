from fastapi import FastAPI
from src.api import produt_api , user_api 

app = FastAPI(description = "API for verify INTELLIGENCE STOCK")

app.include_router(produt_api.product_router,tags = ["Product Tag"])
app.include_router(user_api.user_router , tags = ["User responsable to out or in product"])