from typing import TypedDict

from google.oauth2 import id_token
from google.auth.transport import requests
from django.conf import settings


class GoogleAuthData(TypedDict):
    email: str
    name: str
    email_verified: bool
    picture: str
    given_name: str
    family_name: str
    iss: str
    azp: str
    aud: str
    sub: str
    nbf: int
    iat: int
    exp: int
    jti: str


def verify_google_jwt(token: str) -> GoogleAuthData:
    """
    This functions verifies google credentials
    """
    try:
        return id_token.verify_oauth2_token(
            token, 
            requests.Request(), 
            settings.GOOGLE_OAUTH2_CLIENT_ID
        )
    except ValueError:
        return None
    

# {credential: 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjZjZTExYWVjZjllYjE0MD…O2ymKpiObzpt-N99YRZSTeVhqSRO2_QZoOwU_Zbu10nF17GzA', clientId: '165773732368-pict64818qgurapivi02b0c5lo455pqs.apps.googleusercontent.com', select_by: 'btn'}clientId: "165773732368-pict64818qgurapivi02b0c5lo455pqs.apps.googleusercontent.com"credential: "eyJhbGciOiJSUzI1NiIsImtpZCI6IjZjZTExYWVjZjllYjE0MDI0YTQ0YmJmZDFiY2Y4YjMyYTEyMjg3ZmEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiIxNjU3NzM3MzIzNjgtcGljdDY0ODE4cWd1cmFwaXZpMDJiMGM1bG80NTVwcXMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiIxNjU3NzM3MzIzNjgtcGljdDY0ODE4cWd1cmFwaXZpMDJiMGM1bG80NTVwcXMuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDI0NjAyMzMwMDAyNjc3ODc4NTQiLCJlbWFpbCI6IjE0ODh2YWR5bTIwMDRAZ21haWwuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsIm5iZiI6MTcxMzUyOTUxMSwibmFtZSI6IlZ3dnZ3dnd2d3Z3IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0pPUnAyUjFFeUt0N2dRVWVJZGhYbmRYZ2NMU3g2R2t3YmZMa2VoR3l4YUhCMHVSUT1zOTYtYyIsImdpdmVuX25hbWUiOiJWd3Z2d3Z3dnd2dyIsImlhdCI6MTcxMzUyOTgxMSwiZXhwIjoxNzEzNTMzNDExLCJqdGkiOiJlNzM5NmM0YTgzZDU2ZTA5NDkxOTk1OThkYjU2NTkyYjNjOWNmNTQ1In0.utzydAmXaZWYMfbAiqoG9I4TBEhzFEKdOBqtBJ2Z0D--nYRP1wiu1-veLwSiA7K9hXdrtDTF2W8Koh70GbK7tJ5J0Vfzj9fp3DdWiT_bPYW0w61eR8rOV_hDPJPXdRBeHeu1R_R_VJxh3rvHasQ9ztGQABiB6cbkPLop9E-ozUM2UpgyvJrJIkkM4_snkjblqckDeIKLr92W0K0kAVjXSKnQgqDEJIIAlf_no8f7TUqr_A9o3v_FasDtO8K5BeJPkxOQ-5J7cVLg5fY5RkUXH9QilIzevOQhg1DDIO2ymKpiObzpt-N99YRZSTeVhqSRO2_QZoOwU_Zbu10nF17GzA"select_by: "btn"[[Prototype]]: Object