from schemas import AgentRequest
from responses import success_response

def run_agent_logic(request: AgentRequest):

    return success_response(request.request_id,
                                {
                                    "user_id": request.user_id,
                                    "tool_name": request.tool_name,
                                    "top_k": request.top_k,
                                    "user_preference": request.user_preference,
                                    "answer": f"Received: {request.prompt}"
                                })
