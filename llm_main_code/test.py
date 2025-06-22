import requests
import json
import re














url_chat = "http://10.202.94.52:20232/api/chat"



message = "请输出：这是一个测试"

# print(message)


data = {
    "model": "qwq:latest",
    "messages": [
        {
            "role": "user",
            "content": f"{message}"
        }
    ],
    "stream": False
}

# Send request to the chat API
response = requests.post(url_chat, json=data)
response_dict = json.loads(response.text)

content = response_dict.get('message', {}).get('content', "")

# Define pattern to extract answer
pattern = r'(?<=<\/think>\n\n)(.*)'

match = re.search(pattern, content, re.DOTALL)

print(match.group(1))







