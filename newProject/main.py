from fastapi import FastAPI
from newProject.routers import products, category, cart, order

app = FastAPI()

app.include_router(category.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(order.router)