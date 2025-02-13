from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from routes import chat
from config import settings

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router, prefix="/api")

@app.get("/")
async def root():
    return HTMLResponse("<h1>Minimalist Chatbot API</h1>")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
