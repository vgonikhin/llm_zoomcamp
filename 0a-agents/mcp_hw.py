from fastmcp import FastMCP

import random

known_weather_data = {
    'berlin': 20.0
}

mcp = FastMCP("Demo 🚀")

@mcp.tool
def get_weather(city: str) -> float:
    """
    Retrieves the temperature for a specified city.

    Parameters:
        city (str): The name of the city for which to retrieve weather data.

    Returns:
        float: The temperature associated with the city.
    """
    city = city.strip().lower()

    if city in known_weather_data:
        return known_weather_data[city]

    return round(random.uniform(-5, 35), 1)

#if __name__ == "__main__":
#    mcp.run()

from fastmcp import Client
import asyncio

async def main():
    async with Client("stdio") as mcp_client:
        # TODO
        mcp_client.list_tools_mcp

if __name__ == "__main__":
    test = asyncio.run(main())