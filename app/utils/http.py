import httpx
from tenacity import retry, stop_after_attempt, wait_exponential
from fastapi import Depends
from ..core.config import Settings, get_settings

class HTTPClient:
    def __init__(self, settings: Settings = Depends(get_settings)):
        self.settings = settings
        self.client = httpx.AsyncClient(
            timeout=30.0,
            headers={"Content-Type": "application/json"}
        )

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10)
    )
    async def get(self, url: str, params: dict | None = None) -> dict:
        async with self.client as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()

    async def post(self, url: str, data: dict) -> dict:
        async with self.client as client:
            response = await client.post(url, json=data)
            response.raise_for_status()
            return response.json()