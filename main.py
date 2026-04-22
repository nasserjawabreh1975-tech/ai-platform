from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI PLATFORM RUNNING 🚀"}

@app.post("/task")
def task(task: str):
    return {"task": task, "status": "queued"}
