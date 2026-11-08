import os
import secrets

from fastapi import Depends, HTTPException, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials

ADMIN_USERNAME = 'admin'

security = HTTPBasic()


def require_admin(
    request: Request,
    credentials: HTTPBasicCredentials = Depends(security)
):
    password = os.environ.get('ADMIN_PASSWORD')
    # Stay locked when no password is configured instead of running open.
    if not password:
        raise HTTPException(status_code=503, detail='Set ADMIN_PASSWORD to enable the admin page.')

    username_ok = secrets.compare_digest(credentials.username.encode(), ADMIN_USERNAME.encode())
    password_ok = secrets.compare_digest(credentials.password.encode(), password.encode())
    if not (username_ok and password_ok):
        raise HTTPException(
            status_code=401,
            detail='Incorrect username or password.',
            headers={'WWW-Authenticate': 'Basic'}
        )

    # Browsers resend Basic credentials automatically, so block forms posted from other sites.
    if request.method != 'GET' and request.headers.get('sec-fetch-site') == 'cross-site':
        raise HTTPException(status_code=403, detail='Cross-site requests are not allowed.')
