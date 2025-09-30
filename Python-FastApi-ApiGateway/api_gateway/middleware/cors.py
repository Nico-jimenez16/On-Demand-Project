# app/middleware/cors.py

from starlette.middleware.cors import CORSMiddleware

def setup_cors_middleware(app):
    """
    Configura el middleware de CORS para la aplicación.
    """
    origins = [
        "http://localhost",
        "http://localhost:8000",
        "https://mi-dominio-frontend.com",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],  # Permite todos los métodos HTTP (GET, POST, etc.)
        allow_headers=["*"],  # Permite todos los encabezados
    )