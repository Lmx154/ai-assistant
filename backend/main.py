from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from starlette.requests import Request
from routes import chat, memories
from config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handler to ensure CORS headers are added to error responses
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
         status_code=500,
         content={"detail": str(exc)}
    )

# Include routers
app.include_router(chat.router, prefix="/api")
app.include_router(memories.router, prefix="/api")

@app.get("/")
async def root():
    return HTMLResponse("<h1>Minimalist Chatbot API</h1>")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
