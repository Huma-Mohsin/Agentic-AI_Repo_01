import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(data):
    city = data["city"]
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    res = requests.get(url).json()
    if res.get("main"):
        temp = res["main"]["temp"]
        desc = res["weather"][0]["description"]
        return f"The weather in {city} is {desc} with {temp}°C."
    else:
        return "Could not fetch weather."

def get_top_news(data):
    country = data["country"]
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}&pageSize=3"
    res = requests.get(url).json()
    if res.get("articles"):
        headlines = [article["title"] for article in res["articles"]]
        return "Top News:\n" + "\n".join(f"- {h}" for h in headlines)
    else:
        return "Could not fetch news."
