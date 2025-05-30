import requests                     #API requests library to make HTTP requests 
import json                         #JSON library to parse JSON data
import os                           #OS library to interact with the operating system
from dotenv import load_dotenv      #Load environment variables from a .env file

#Step 2: Load the API Key from .env

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('OPENROUTER_API_KEY')  # Get the API key from the environment variable
#.env file mein jo API key store ki thi, usse secure tarike se load kiya gaya.

#Step 3: Define OpenRouter API Endpoint
url = "https://openrouter.ai/api/v1/chat/completions" # OpenRouter API endpoint for chat completions,Ye OpenRouter ka endpoint URL hai jahan hum request bhej rahe hain.

#Step 4: Create the Message Payload
user_input = input("Ask something: ")
payload = {
    "model": "openai/gpt-4",
    "messages": [
        {
            "role": "system",  #behavior or persona of the AI assistant.
            "content": "You are a helpful assistant who provides clear and concise explanations."
        },
        {
           "role": "user",
            "content": user_input
        }
    ],
    # parameters in the payload — they help control the quality, style, and length of the AI’s response:

    "temperature": 0.7,  #controls the randomness of the output. Higher values make the output more random, while lower values make it more focused and deterministic.

    "max_tokens": 250,   #maximum number of tokens (words or word pieces) in the response.

    "top_p": 1,  #controls the diversity of the output. It is an alternative to temperature, where 1 means all tokens are considered, and lower values restrict the selection to a subset of tokens.

    "frequency_penalty": 0, #penalizes new tokens based on their frequency in the text so far. Higher values discourage repetition.

    "presence_penalty": 0 #penalizes new tokens based on whether they appear in the text so far. Higher values encourage the model to talk about new topics.
}

#Step 5: Set the Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",  # means , Yeh request meri hai, yeh mera secret token hai, mujhe access do
    "Content-Type": "application/json" #Content-Type header se API ko pata chalta hai ke aapka data kis format mein hai (yahan JSON), taki wo sahi se process kar sake.
}

#Step 6: Send the Request to OpenRouter
response = requests.post(url, headers=headers, data=json.dumps(payload)) # #POST request bhej rahe hain OpenRouter API ko, jahan humne URL, headers aur payload specify kiya hai.Ye line hamara prepared message AI ko bhejti hai.

#Step 7: Handle the Response
if response.status_code == 200:
    result = response.json()
    print("Assistant says:\n")
    print(result["choices"][0]["message"]["content"])
else:
    print(" Error occurred:")
    print(f"Status Code: {response.status_code}")
    print(response.text)

#Agar sab kuch theek hua (status_code == 200), to AI ka response print hoga.
#Agar koi error aayi to status code aur error details print honge.





