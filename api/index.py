import json
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Load marks data from marks.json (which is in the same folder)
with open("marks.json") as f:
    marks_data = json.load(f)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = [marks_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
