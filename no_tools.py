from groq import Groq
from dotenv import load_dotenv


load_dotenv()
client = Groq()


prompt = "what is 48,173 * 92,861? reply with only the number."

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
                "content": prompt
        }
    ],
    model="openai/gpt-oss-20b"
)

""""
print(chat_completion.choices[0].message.content)
print(chat_completion.choices[0].finish_reason)
print(chat_completion.choices[0].message)
"""

print(92861 *173)