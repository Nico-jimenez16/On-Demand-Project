from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Configuración general de la app
    app_name: str
    app_description: str
    app_version: str
    app_env: str
    app_host: str 
    app_port: int

    # URLs de los microservicios
    AUTH_SERVICE_URL: str
    USERS_SERVICE_URL: str
    REQUEST_SERVICE_URL: str

    # Seguridad y autenticación
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env"  # Archivo de variables de entorno
        env_file_encoding = "utf-8"

# Crear instancia de settings para usar en toda la app
settings = Settings()
