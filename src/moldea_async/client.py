import httpx


class Moldea:
    def __init__(self, base_url: str = "https://httpbin.org") -> None:
        self.base_url = base_url.rstrip("/")

    async def get(self) -> dict:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(f"{self.base_url}/get")
            response.raise_for_status()
            return response.json()