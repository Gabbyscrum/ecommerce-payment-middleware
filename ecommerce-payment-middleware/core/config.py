

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Ecommerce Payment Middleware"
    ENV: str = "dev"
    
    # Providers
    STRIPE_SECRET_KEY: str | None = None
    PAYSTACK_SECRET_KEY: str | None = None

    # Security
    API_KEY: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()
