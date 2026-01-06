from fastapi import FastAPI
from routes import user_routes, auth_routes, product_routes

app= FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])

app.include_router(product_routes.router, prefix="/products", tags=["Product"])