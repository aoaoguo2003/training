import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


url = "http://127.0.0.1:8000/agent/run"

payload = {
    "request_id": "req-001",
    "user_id": "user-001",
    "prompt": "Please analyse this request",
    "tool_name": "search"
}


def call_agent_api(url: str, payload: dict):
    try:
        logger.info("calling agent API url=%s request_id=%s",
                    url,
                    payload.get("request_id"))
        response = requests.post(
            url,
            json=payload,
            timeout=5
        )

        response.raise_for_status()

        result = response.json()
    
        logger.info(
            "agent API completed request_id=%s success=%s",
            payload.get("request_id"),
            result.get("success")
        )

        return result

    except requests.Timeout:
        logger.error(
            "agent API timeout url=%s request_id=%s",
            url,
            payload.get("request_id")
        )
        return None
    
    except requests.HTTPError as error:
        logger.error(
            "agent API HTTP error url=%s request_id=%s error=%s",
            url,
            payload.get("request_id"),
            error
        )

        if error.response is not None:
            print("response body:", error.response.json())

        return None

    except requests.RequestException as error:
        logger.error(
            "agent API request failed url=%s request_id=%s error=%s",
            url,
            payload.get("request_id"),
            error
        )
        return None
    
result = call_agent_api(url, payload)
print(result)