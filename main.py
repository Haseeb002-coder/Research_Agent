
# ============== internal console run code ==============

# from src.graph import graph_bilder

# user = input("Enter Question: ")

# graph = graph_bilder(user)

# print(graph)

# ===============================



# ===================== frontened code with Html k sath ========================



from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from src.graph import graph_bilder

app = FastAPI()

# Serve static files (like index.html)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the HTML frontend at root path
@app.get("/")
def read_index():
    return FileResponse("static/index.html")

# Request model
class QuestionInput(BaseModel):
    question: str

# Route for graph generation
@app.post("/generate-graph")
def generate_graph(data: QuestionInput):
    try:
        graph = graph_bilder(data.question)
        return {"graph": graph}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
