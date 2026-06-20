import logging
import json
import time

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def analyse_calls(filename):
    with open(filename, "r", encoding = 'utf-8') as file:
        calls = json.load(file)

        logger.info("program started filename=%s", filename)



        for call in calls:
            tool_name = call["tool"]
            latency = call["latency"]
            success = call['success']
            if call["latency"] > 1:
                logger.warning("tool latency(%s) is too high(%s)", tool_name, latency)

            if call['success'] == False:
                logger.error('tool(%s) failed', tool_name)


class Tool:
    def __init__(self, name):
        self.name = name
        self.call_count = 0

    def call(self):
        logger.info(
            "call started tool=%s call_count=%d",
            self.name,
            self.call_count
            )
        
        self.call_count += 1

        logger.info("call num +1 tool=%s call_count=%d",
            self.name,
            self.call_count
            )

    def get_info(self):
        return {
            "name": self.name,
            "call_count": self.call_count
        }



def load_json_file(filename: str):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data
    
    except FileNotFoundError:
        logger.error("file not found error filename=%s", filename)
        return None

    except json.JSONDecodeError:
        logger.exception("json decode error filename=%s", filename)
        return None


def run_agent(request_id: str, tool_name: str) -> dict:
    logger.info("request id=%s, tool name=%s", request_id, tool_name)

    start_time = time.perf_counter()

    time.sleep(2)

    end_time = time.perf_counter()

    latency = end_time - start_time

    logger.info(
        "request completed request_id=%s tool=%s latency=%.2f",
        request_id,
        tool_name,
        latency
    )
    return {
        "request_id": request_id,
        "tool": tool_name,
        "success": True,
        "latency": latency
    }

#debug, warning, error, debug, error