from django.conf import settings

def set_jwt_cookies(response, access_token, refresh_token):
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE"],
        value=access_token,
        httponly=True,
        secure=True,
        samesite="Lax",
        path="/"
    )
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
        value=refresh_token,
        httponly=True,
        secure=True,
        samesite="Lax",
        path="/"
    )
    return response
