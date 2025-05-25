# Payment Middleware Service

Provider-agnostic payment gateway written in Python.

## Features
- Multiple payment providers
- Idempotent requests
- Webhook verification
- Secure API key auth

## Run
pip install -r requirements.txt
uvicorn app.main:app --reload
