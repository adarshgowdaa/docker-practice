from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "My Docker Container is running successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
