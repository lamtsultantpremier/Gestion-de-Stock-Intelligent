from fastapi import FastAPI
from src.api import user_api , categorie_api , product_api

app = FastAPI(description = "API for verify INTELLIGENCE STOCK")

app.include_router(product_api.product_router, tags = ["Product Tag"])
app.include_router(user_api.user_router , tags = ["User responsable to out or in product"])
app.include_router(categorie_api.categorie_router , tags =["Product Categories"])