from typing import TypedDict

import requests


class GoogleAccessTokenResponse(TypedDict):
    id: str
    email: str
    verified_email: bool
    name: str
    given_name: str
    family_name: str
    picture: str
    locale: str


def verify_google_access_token(token: str) -> GoogleAccessTokenResponse:
    """
    This functions verifies google access token
    """
    url = f"https://www.googleapis.com/oauth2/v1/userinfo?access_token={token}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# example
# https://www.googleapis.com/oauth2/v1/userinfo?access_token=ya29.a0AXooCgu2P0BhFKWcxjQ6ch1LMHGlFKg-M2kf912FlU_ZoyKZvbJRVx5XYWgbbDS7I_-l-VyIxgd6oS_kdoiHC97ZeEsdknXozJOotR3sQElvIfJxxycivb7qDi2HVyc1agXcfz6IfANB2sy9-idX1CTEU_9l9I2ClwaCgYKAQwSARESFQHGX2MiT1kBW5U_pnEbYq1SPnU4wA0169
