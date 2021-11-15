def my_jwt_response_payload_handler(token, user, request):
    return {
        "code": 200,
        "data": {"token": token},
    }
