import os
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def get_my_ip():
    api_type = os.environ.get("TYPE", "API1")

    if api_type == "API1":
        url = "http://ip-api.com/json/"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            ip = data.get("query")

    elif api_type == "API2":
        url = "https://jsonip.com"
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            data = response.json()
            ip = data.get("ip")

    else:
        raise HTTPException(status_code=400)

    return {"myIP": ip, "apiType": api_type}
