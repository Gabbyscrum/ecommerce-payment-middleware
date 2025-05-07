from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Payment Middleware"
    API_KEY: str = "dev_key"

    STRIPE_SECRET_KEY: str = ""
    STRIPE_WEBHOOK_SECRET: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
