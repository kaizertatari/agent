from groq import Groq
from dotenv import load_dotenv
import json
from tools import multiply
load_dotenv()
client = Groq()


prompt = "what is 48,173 * 92,861?"
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
print(type(args))
print(args["a"])
print(chat_completion.choices[0].message.tool_calls[0].function) 