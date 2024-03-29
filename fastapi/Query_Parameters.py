from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items" : [{"items_id" : "Foo"}, {"item_id" : "Bar"}]}
    if q:
        results.update({"q":q})
    return results