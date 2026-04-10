from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    nice_base_url: str = "https://example.nice.api"
    nice_client_id: str = "dev-client"
    nice_api_key: str = "dev-key"
    db_url: str = "sqlite+aiosqlite:///./nice_api.db"
    redis_url: str = "redis://localhost:6379/0"
    chunk_size: int = 500
    chunk_delay_seconds: float = 0.5

    model_config = SettingsConfigDict(
        env_file=".env.dev",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()
