import httpx
from .base import IPService

class JsonIpService(IPService):
    async def get_ip(self) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://jsonip.com")
            data = response.json()
            return data.get("ip")
