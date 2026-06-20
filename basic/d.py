#1
def safe_divide(a:float, b: float):
    if b == 0:
        return None;
    else:
        return a/b
#2
def parse_int(text: str):
    try:
        num = int(text)
        return num
    except ValueError:
        return None
#3  
import json

def load_json_file(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
    
    except FileNotFoundError:
        print("file not exist")
        return None

    except json.JSONDecodeError:
        print("Json format error")
        return None
#4 
calls = [
    {"tool": "search", "latency": 1.2, "success": True},
    {"tool": "weather", "success": False},
    {"tool": "calculator", "latency": 0.3, "success": True}
]

total_latency = 0
for call in calls:
    latency = call.get('latency')

    if latency is None:
        continue
    else:
        total_latency += latency

print(total_latency)

#5
#会遇到分母不能为0，因为输入的参数的长度为0