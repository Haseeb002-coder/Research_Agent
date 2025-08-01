from fastapi import FastAPI, Request
from pydantic import BaseModel
from src.graph import graph_bilder

app = FastAPI()

# Input model
class Question(BaseModel):
    user: str

@app.post("/get-graph")
def get_graph(data: Question):
    graph = graph_bilder(data.user)
    return {"graph": graph}
