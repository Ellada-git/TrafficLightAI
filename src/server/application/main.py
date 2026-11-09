from fastapi import FastAPI

app = FastAPI(
    title="TrafficLightAI API",
    description="API системы интеллектуального управления светофорами",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "message": "TrafficLightAI server is running",
        "status": "ok",
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
    }