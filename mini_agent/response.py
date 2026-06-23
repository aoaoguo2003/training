def analysis_tool_results(results):
    success_count = 0
    failure_count = 0
    timeout_count = 0

    for result in results:
        if result["success"]:
            success_count += 1
        else:
            failure_count += 1
        
        if result["error_type"] == "TIMEOUT":
            timeout_count += 1

    return {
        "total_tools": len(results),
        "success_count": success_count,
        "failure_count": failure_count,
        "timeout_count": timeout_count
    }