# #Number validations: greater than or equal
# from typing import Optional

# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(..., title="The ID of the item to get", ge=1), q:str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results

# #Number validations: greater than and less than or equal
# from typing import Optional

# from fastapi import FastAPI, Path, Query

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000), q:str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     return results

#Number vakudationsL floats, greater than and less than
from typing import Optional

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", gt=0, le=1000), 
    q:str,
    size: float =Query(..., gt=0, lt=0.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q":q})
    return results