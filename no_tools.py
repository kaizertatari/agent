from groq import Groq
from dotenv import load_dotenv



load_dotenv()
client = Groq()

prompt = {"tool" : "delete_files", "a" : "48173", "b" : "92861"}


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
""""