from typing import Dict, Any
from django.conf import settings
from django.core.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
import requests
import json

GOOGLE_ID_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_ACCESS_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


def generate_tokens_for_user(user):
    """
    Generate access and refresh tokens for the given user
    """
    serializer = TokenObtainPairSerializer()
    token_data = serializer.get_token(user)
    access_token = token_data.access_token
    refresh_token = token_data
    return access_token, refresh_token


def google_get_access_token(code: str, redirect_uri: str) -> str:
    # data = {
    #     "code": code,
    #     "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
    #     "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
    #     "redirect_uri": redirect_uri,
    #     "grant_type": 'authorization_code'
    # }

    payload = json.dumps({
        "code": "4/0AeaYSHBOjH_GIqUQEJK_3izkPL2HjOa5OpRQtdvtL8aJJyxlwUIMetkZP_elmknzabGVjw",
        "client_id": "98679761827-8r4lgrfgttj0kco2rljsmranfbf028la.apps.googleusercontent.com",
        "client_secret": "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",
        "redirect_uri": "postmessage",
        "grant_type": "authorization_code"
    }
    )
    print(payload)
    print(GOOGLE_ACCESS_TOKEN_OBTAIN_URL)
    response = requests.request("POST", GOOGLE_ACCESS_TOKEN_OBTAIN_URL, data=payload)
    if not response.ok:
        raise ValidationError('Failed to obtain access token from Google.')
    access_token = response.json()['access_token']
    print(access_token)
    return access_token


def google_get_user_info(*, access_token: str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )

    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    return response.json()
