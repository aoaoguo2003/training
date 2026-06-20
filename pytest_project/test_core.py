from core import normalize_tool_name
from core import Tool, Agent, analyse_calls
import pytest

def test_normalize_tool_name():
    result = normalize_tool_name("  HELlo ")
    assert result == "hello"

def test_normal_tool_name():
    result = normalize_tool_name("hello")
    assert result == "hello"

def test_only_have_spaces():
    result = normalize_tool_name("  ")
    assert result == ""

def test_initial_call_iszero():
    initial_call = Tool("a").call_count
    assert initial_call == 0

def test_call_is_2():
    a = Tool("a")
    a.call()
    a.call()
    call_count = a.call_count
    assert call_count == 2

def test_get_info():
    a = Tool("a")
    assert a.get_info() == {
        "name": "a",
        "call_count": 0
    }

def test_agent_able_retry():
    agent = Agent("agent", 2)
    assert agent.can_retry() == True

def test_callnum_after_one():
    agent = Agent("agent", 2)
    agent.increase_retry()
    assert agent.retry_count == 1

def test_max_cannnot_retry():
    agent = Agent("agent", 2)
    agent.increase_retry()
    agent.increase_retry()
    agent.increase_retry()

    assert agent.can_retry() == False



def test_analysis_calls_total_calls():
    calls = [
    {"tool": "search", "latency": 1.2, "success": True},
    {"tool": "weather", "latency": 2.3, "success": False},
    {"tool": "search", "latency": 0.8, "success": True}
    ]
    
    analysized_calls = analyse_calls(calls)
    assert analysized_calls["total_calls"] == 3
    assert analysized_calls["success_count"] == 2
    assert analysized_calls["failure_count"] == 1
    assert analysized_calls["total_latency"] == pytest.approx(4.3)
    assert analysized_calls["unique_tools"] == ["search", "weather"]

