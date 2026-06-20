prompt = "Please analyse this request"
user_id = "user-001"

headers = {
    'Content-Type': 'application/json'
}

payload = {
    "prompt" : prompt,
    "user_id" : user_id
}

import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

def fetch_json(url: str):
    try:
        response = requests.get(url, timeout=5)

        response.raise_for_status()

        return response.json()
    except requests.Timeout:
        logger.error("request timeout, url=%s", url)

    except requests.RequestException:
        logger.error("request failed, url=%s", url)

#401是未认证，未登录，想要访问已登录的数据
#403是认证了，登录了，但是权限不够
#429是限流了，比如前端太多人请求调取api
#500是后端有bug
#502是中间代理拿不到后端响应
#504是后端太慢，超时

#5前端向后端提交一次分析请求，包含人脸信息，客户偏好，后端返回的是根据这些信息计算后的分析结果