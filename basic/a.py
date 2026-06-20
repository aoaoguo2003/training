#1
tools = ["search", "weather", "calculator"]

print(tools[0])

tools[1] = "database"

tools.append("email")

print(tools)

#2读取字典
agent_result = {
    "status": "success",
    "latency": 1.5,
    "tool_name": "search"
}

print(agent_result['status'])

agent_result["latency"] = 2.0

agent_result['retry_count'] = 0

print(agent_result)

#3 列表中包含字典
calls = [
    {"tool": "search", "success": True},
    {"tool": "weather", "success": False},
    {"tool": "calculator", "success": True}
]
success_num = 0
for call in calls:
    if call['success'] == True:
        success_num += 1
print(success_num)

#4 工具去重
tools = ["search", "weather", "search", "calculator", "weather"]

unique_tools = set(tools)
print(unique_tools)

#5 综合函数
calls = [
    {"tool": "search", "latency": 1.2, "success": True},
    {"tool": "weather", "latency": 2.3, "success": False},
    {"tool": "search", "latency": 0.8, "success": True}
]

def analyse_calls(calls: list[dict]) -> dict:
    total_calls = len(calls)
    success_calls = 0
    total_latency = 0
    unique_tools = set()

    for call in calls:
        if call['success']:
            success_calls += 1

        total_latency += call['latency']

        unique_tools.add(call['tool'])

    return {
        "total_calls": total_calls,
        "success_count": success_calls,
        "total_latency": total_latency,
        "unique_tools": unique_tools
}

print(analyse_calls(calls))