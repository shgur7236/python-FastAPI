# #요청 본문 선언의 고급 사용법


# #Mix Path, Query and body paprameters
# from typing import Optional

# from fastapi import FastAPI, Path
# from pydantic import BaseModel

# app=FastAPI()

# class Item(BaseModel):
#     name:str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# @app.put("/items/{item_id}")
# async def update_item(
#   *,
#   item_id: int = Path(..., title="The Id of the item to get", ge=0, le=1000),
#   q:  Optional[str]= None,
#   item: Optional[Item] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"q": q})
#     return results


# #Multiple body parameters
# from typing import Optional

# from fastapi import Body,FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None

# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int, item: Item, user: User, importance: int = Body(...)):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results


#Multiple body params and query
# from typing import Optional

# from fastapi import Body, FastAPI
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None


# class User(BaseModel):
#     username: str
#     full_name: Optional[str] = None


# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int,
#     item: Item,
#     user: User,
#     importance: int = Body(..., gt=0),
#     q: Optional[str] = None
# ):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     if q:
#         results.update({"q": q})
#     return results


#Embed a single body parameter

from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}