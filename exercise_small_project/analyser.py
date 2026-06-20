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