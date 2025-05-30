import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

from tools import get_weather, get_top_news  # Same custom functions you wrote

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


def tool_response(user_input: str):
    # Simple trigger logic to call tools
    if "weather" in user_input.lower():
        city = user_input.split("in")[-1].strip() if "in" in user_input else "Karachi"
        return get_weather({"city": city})

    elif "news" in user_input.lower():
        country = user_input.split("from")[-1].strip() if "from" in user_input else "us"
        return get_top_news({"country": country})

    return None


async def main():
    print("🤖 Gemini Assistant (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            break

        tool_result = tool_response(user_input)

        if tool_result:
            print(f"\n🔧 Tool: {tool_result}")
            prompt = f"{user_input}\n\nTool result: {tool_result}"
        else:
            prompt = user_input

        response = model.generate_content(prompt)
        print(f"\n🤖 Gemini: {response.text}")


if __name__ == "__main__":
    asyncio.run(main())
