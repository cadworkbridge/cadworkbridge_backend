from django.conf import settings

def set_jwt_cookies(response, access_token, refresh_token):
    access_max_age = int(settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds())
    refresh_max_age = int(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds())

    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE"],
        value=access_token,
        max_age=access_max_age,
        httponly=True,
        secure=True,
        samesite="Lax",
        path="/"
    )
    response.set_cookie(
        key=settings.SIMPLE_JWT["AUTH_COOKIE_REFRESH"],
        value=refresh_token,
        max_age=refresh_max_age,
        httponly=True,
        secure=True,
        samesite="Lax",
        path="/"
    )
    return response
