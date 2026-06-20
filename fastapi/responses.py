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

def success_response(request_id: str, data: dict) -> dict:
    return {
        "success": True,
        "request_id": request_id,
        "data": data,
        "error": None
    }