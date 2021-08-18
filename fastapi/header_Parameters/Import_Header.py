from typing import Optional

from fastapi import FastAPI, Header

app= FastAPI()

@app.get("/itmes/")
async def read_items(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}