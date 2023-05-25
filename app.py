import pandas as pd
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from typing import List

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Sample data for demonstration
data = {
    "id": [1, 2, 3],
    "title": ["Example Link 1", "Example Link 2", "Example Link 3"],
    "comment_cnt": [10, 5, 15],
    "points": [50, 20, 100],
    "clicked": [False, False, False]
}

df = pd.DataFrame(data)

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "links": df.to_dict("records")})

@app.get("/click/{link_id}")
def click_link(link_id: int):
    df.loc[df["id"] == link_id, "clicked"] = True
    return {"message": "Link clicked!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000,)
