from typing import Tuple

from starlette.authentication import AuthCredentials, AuthenticationBackend, AuthenticationError, SimpleUser
import base64
import binascii

from starlette.requests import HTTPConnection
from starlette.responses import RedirectResponse
from starlette.status import HTTP_401_UNAUTHORIZED


class BasicAuthBackend(AuthenticationBackend):
    async def authenticate(
            self,
            conn: HTTPConnection,
    ) -> RedirectResponse | None | tuple[AuthCredentials, SimpleUser]:
        path = conn.scope["path"]
        print(path)
        if "Authorization" not in conn.headers and path not in ["/"]:
            return RedirectResponse(url="/")
        """
        auth = conn.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() != "basic":
                return None
            decode = base64.b64decode(credentials).decode("ascii")
        except(ValueError, UnicodeDecodeError, binascii.Error) as exc:
            raise AuthenticationError("Invalid basic auth credentials")

        username, _, password = decode.partition(":")
        return AuthCredentials(["authenticated"]), SimpleUser(username)
        """
