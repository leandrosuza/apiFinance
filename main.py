from fastapi import FastAPI

app = FastAPI(title="Cuida Finance API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "Cuida Finance API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
