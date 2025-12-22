from fastapi import FastAPI, HTTPException
from app.config import API_TYPE
from app.services.ip import IpApiService
from app.services.json import JsonIpService
from app.services.base import IPService

app = FastAPI()

def get_ip_service() -> IPService:
    if API_TYPE == "API1":
        return IpApiService()
    elif API_TYPE == "API2":
        return JsonIpService()
    else:
        raise HTTPException(status_code=400)


@app.get("/")
async def get_my_ip():
    service = get_ip_service()
    ip = await service.get_ip()
    return {"myIP": ip, "apiType": API_TYPE}

