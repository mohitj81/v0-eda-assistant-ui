from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import upload, profiling, risk, explain, script, compare

app = FastAPI(title="EDA Assistant Backend", version="1.0")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(upload.router)
app.include_router(profiling.router)
app.include_router(risk.router)
app.include_router(explain.router)
app.include_router(script.router)
app.include_router(compare.router)

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/")
def root():
    return {"message": "EDA Assistant Backend Running"}
