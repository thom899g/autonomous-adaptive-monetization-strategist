import aiohttp

class MarketAnalyzer:
    def __init__(self):
        self.session = None
        
    async def fetch_data(self):
        try:
            self.session = aiohttp.ClientSession()
            async with self.session.get('https://api.markets.com/trends') as response:
                data = await response.json()
                return data
        except Exception as e:
            raise MarketDataFetchError(f"Failed to fetch market data: {str(e)}")