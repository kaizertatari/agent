def run_tool(args,name):
    if(name == "multiply"):
        return multiply(args.get('a'),args.get('b'))
    else:
        return f"Error: unknown tool '{name}'"

def multiply(a,b):
    if not isinstance(a, (int,float)) :
        return f"Error:'a' must be a number , got {a}"
    elif not isinstance (b, (int,float)):
        return f"Error:'b' must be a number , got {b}"
    else:
        return a * b
    
if __name__ == "__main__":
    request = {"tool" : "divide", "a" : 48173, "b" : 40}
    print(run_tool(request, request["tool"]))