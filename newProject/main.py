from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware
from newProject.routers import products, category, cart, order

app = FastAPI()

from fastapi import FastAPI
from newProject.routers import products, category, cart, order

app = FastAPI()
# ---------------- CORS Middleware ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change later for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Logging Middleware ----------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    request_id = str(uuid.uuid4())

    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id

    process_time = time.time() - start_time
    print(f"{request.method} {request.url} - {process_time:.4f}s")

    return response


# ---------------- Routers ----------------

app.include_router(category.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(order.router)