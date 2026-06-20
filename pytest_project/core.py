def normalize_tool_name(tool_name: str) -> str:
    return tool_name.strip().lower()

class Tool:
    def __init__(self, name):
        self.name = name
        self.call_count = 0

    def call(self):
        self.call_count += 1

    def get_info(self):
        return {
            "name": self.name,
            "call_count": self.call_count
        }
    
class Agent:
    def __init__(self, name, max_retries):
        self.name = name
        self.max_retries = max_retries
        self.retry_count = 0

    def can_retry(self):
        if self.retry_count < self.max_retries:
            return True
        else:
            return False
        
    def increase_retry(self):
        if self.can_retry() == True:
            self.retry_count += 1

    def to_dict(self):
        return {
            "name": self.name,
            "max_retries": self.max_retries,
            "retry_count": self.retry_count
        }
    
def analyse_calls(calls: list[dict]) -> dict:
    total_calls = 0
    success_count = 0
    failure_count = 0
    total_latency = 0
    unique_tools = []

    for call in calls:
        if "tool" not in call or "latency" not in call or "success" not in call:
            continue
        
        total_calls += 1
        if call['success']:
            success_count += 1
        else:
            failure_count += 1
        
        total_latency += call['latency']

        if call["tool"] not in unique_tools:
            unique_tools.append(call["tool"])

    return {
        "total_calls": total_calls,
        "success_count": success_count,
        "failure_count": failure_count,
        "total_latency": total_latency,
        "unique_tools": unique_tools
    }