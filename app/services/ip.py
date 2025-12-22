import httpx
from .base import IPService

class IpApiService(IPService):
    async def get_ip(self):
        async with httpx.AsyncClient() as client:
            response = await client.get("http://ip-api.com/json/")
            data = response.json()
            return data.get("query")
