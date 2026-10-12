from groq import Groq
from dotenv import load_dotenv
import json
from tools import run_tool
load_dotenv()
client = Groq()


prompt = "what's 12 × 7, and what's 300 × 41?"
tools = [
    {
        "type": "function",
        "function": {
            "name": "multiply",
            "description": "Multiply two numbers. Use this for any multiplication.",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "number", "description": "First number"},
                    "b": {"type": "number", "description": "Second number"},
                },
                "required": ["a", "b"],
            },
        }, 
    }
]


chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
                "content": prompt
        }
    ],
    model="openai/gpt-oss-20b",
    tools= tools
)

args = json.loads(chat_completion.choices[0].message.tool_calls[0].function.arguments)

tool_name = chat_completion.choices[0].message.tool_calls[0].function.name

answer =run_tool(args,tool_name)

tool_call = chat_completion.choices[0].message.tool_calls[0].id

prompt ={"role":"user", "content":prompt}
answer = {"role":"tool", "tool_call_id":tool_call, "content":str(answer)}
messages =[]
messages.append(prompt)
messages.append(chat_completion.choices[0].message)
messages.append(answer)

chat_2 = client.chat.completions.create(
    messages= messages,
    model="openai/gpt-oss-20b",
    tools= tools
)
#print(chat_2.choices[0].message)
#print(chat_2.choices[0].message.content)
print(chat_completion.choices[0].message)
