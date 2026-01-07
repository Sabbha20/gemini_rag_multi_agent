from dotenv import load_dotenv
import os

from langchain.tools import tool
import ollama
import requests

load_dotenv()

# ---------------------------
# Web Search Tool
# ---------------------------
@tool
def z_web_search(query: str):
    """
    Perform live web search using ollama

    Args:
        query (str): search query string
    Returns:
        JSON string of top results (max 2)
    """
    response = ollama.web_search(query=query, max_results=2)
    results = response.results
    
    return results

# ---------------------------
# Weater API Tool
# ---------------------------
@tool
def z_get_weater(location: str):
    """Get current weater for a location using WeatherAPI.com
    Use for queries about weather, temeparature, or condition in any city
    For Example: "weather in Paris", "temperature in tokyo", "is it raining in Kolkata"

    Args:
        location (str): city name (e.g., "London", "New York")
    Returns:
        Current weather description string, including temperature and condition
    """

    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('WEATHER_API_KEY')}&q={location}&aqi=yes"
    
    response = requests.get(url=url, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    
    return data 
