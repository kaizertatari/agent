from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

request = {"tool" : "delete_files", "a" : 48173, "b" : 92861}

def multiply(a,b):
    
    return a * b
if request["tool"] == "multiply":
    print(multiply(request["a"], request["b"]))
else:
    print("Unknown tool")



