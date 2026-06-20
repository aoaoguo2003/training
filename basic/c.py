#1
errors = ["timeout", "database", "validation"]

with open('errors.txt', 'w', encoding = 'utf-8') as file:
    for error in errors:
        file.write(f"{error}\n")

#2
with open("errors.txt", 'r', encoding = 'utf-8') as file:
    errors = file.read().split()

error_counts = {}
for error in errors:
    error_counts[error] = error_counts.get(error, 0) + 1


print(error_counts)

#3
import json

report = {
    "total_calls": 5,
    "success_count": 4,
    "failure_count": 1
}

with open('report.json', 'w', encoding = 'utf-8') as file:
    json.dump(report, file, indent=2, ensure_ascii=False)

#4
with open("report.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

print(data['total_calls'])
print(data['success_count'])
print(data['failure_count'])

#5
with open("calls.json", "r", encoding = "utf-8") as file:
    calls = json.load(file)

total_calls = len(calls)
success_count = 0
failure_count = 0
total_latency = 0
unique_tools = set()


for call in calls:
    if call['success']:
        success_count += 1
    else:
        failure_count += 1
    
    total_latency += call['latency']

    unique_tools.add(call['tool'])

analysis = {
    'total_calls': total_calls,
    "success_count": success_count,
    "failure_count": failure_count,
    'total_latency': total_latency,
    "unique_tools": list(unique_tools)
}

print(analysis)

with open('analysis.json', 'w', encoding='utf-8') as file:
    json.dump(analysis, file, ensure_ascii=False, indent=2)