from fastapi import FastAPI
from .core.settings import settings

#! Middlewares - Imports
from .middleware.authentication import AuthMiddleware
from .middleware.cors import CORSMiddleware
from .middleware.logging import LoggingMiddleware

#! Rutas - Imports
from .api.endpoints import auth_routes, user_routes, service_request_routes

app = FastAPI(
    title=settings.app_name, 
    description= settings.app_description, 
    version=settings.app_version
    )

#! Middlewares de seguridad de la aplicación:

# CORS: Primero CORS -  Para manejar los encabezados de pre-vuelo   y permitir solicitudes desde orígenes específicos.
# Autenticación: Segundo AuthMiddleware - Para validar tokens de autenticación en las solicitudes entrantes.
# Logging: Tercero LoggingMiddleware - Para registrar detalles de cada solicitud y respuesta.

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://mi-dominio-frontend.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agregar middleware de autenticación
app.add_middleware(AuthMiddleware)

# Agregar middleware de logging
app.add_middleware(LoggingMiddleware)

#!   Incluir rutas
#app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])
#app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(service_request_routes.router, prefix="/requests", tags=["Service Requests"])

@app.get("/")
def health_check():
    return {"status": "ok", "service": settings.app_name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_gateway.main:app", host="127.0.0.1", port=settings.app_port, reload=True)
