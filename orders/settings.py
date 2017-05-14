from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

AUTHENTICATION_CLASSES = (
    TokenAuthentication,
)

PERMISSION_CLASSES = (
    IsAuthenticated,
)
