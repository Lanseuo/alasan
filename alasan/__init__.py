# Card Type (Response)
SIMPLE = "Simple"
STANDARD = "Standard"
LINK_ACCOUNT = "LinkAccount"
ASK_FOR_PERMISSIONS_CONSENT = "AskForPermissionsConsent"

from .core import Alasan  # noqa
from .response import Response  # noqa

__all__ = ["Alasan", "Response"]
