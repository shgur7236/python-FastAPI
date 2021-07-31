from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()

# Alias는 경로를 찾아준다
@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
