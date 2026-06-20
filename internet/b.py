import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def success_response(request_id: str, data: dict) -> dict:
    return {
        "success": True,
        "request_id": request_id,
        "data": data,
        "error": None
    }

def error_response(
    request_id: str,
    code: str,
    message: str
) -> dict:
    return {
            "success": False,
            "request_id": request_id,
            "data": None,
            "error": {
                "code": code,
                "message": message
            }
    }


def post_json(
    url: str,
    payload: dict,
    headers: dict | None = None,
    timeout: int = 30
):
    try:

        response = requests.post(url, json=payload, headers= headers, timeout= timeout)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.Timeout:
        logger.error("time out error, url=%s", url)
        return None
    
    except requests.exceptions.RequestException:
        logger.error("request error, url=%s", url)
        return None
    
def run_agent_logic(
    request_id: str,
    user_id: str,
    prompt: str
) -> dict:
    if not prompt.strip():
        return error_response("req-001", "INVALID_INPUT", "prompt can not be empty")
    
    else:
        return success_response(request_id,
                                {
                                    "user_id": user_id,
                                    "answer": f"Received: {prompt}"
                                })
    
request_id = "req-001"
user_id = "user-001"
prompt = "Please analyse this request"

result = run_agent_logic(request_id, user_id, prompt)
print(result)