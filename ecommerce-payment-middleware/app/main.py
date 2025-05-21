from fastapi import FastAPI
from app.api.routes import payments, webhooks, health
from app.middleware.request_id import request_id_middleware

app = FastAPI(title="Payment Middleware")

app.middleware("http")(request_id_middleware)

app.include_router(payments.router)
app.include_router(webhooks.router)
app.include_router(health.router)
