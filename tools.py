from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq()

request = {"tool" : "multiply", "a" : 48173, "b" : "forty"}

def multiply(a,b):
    if not isinstance(a, (int,float)) :
        return f"Error:'a' must be a number , got {a}"
    elif not isinstance (b, (int,float)):
        return f"Error:'b' must be a number , got {b}"
    else:
        return a * b

if request["tool"] == "multiply":
    print(multiply(request["a"], request["b"]))
else:
    print("Unknown tool")