from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import graph_bilder

app = FastAPI()

# Request model
class QuestionInput(BaseModel):
    question: str

# Route
@app.post("/generate-graph")
def generate_graph(data: QuestionInput):
    try:
        graph = graph_bilder(data.question)
        return {"graph": graph}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
