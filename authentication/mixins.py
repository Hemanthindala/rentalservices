# mixins.py

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions

from django.core.exceptions import ValidationError

from .models import User


class ApiAuthMixin:
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )


class PublicApiMixin:
    authentication_classes = ()
    permission_classes = ()


from rest_framework.views import exception_handler
from rest_framework.response import Response

class ApiErrorsMixin:
    expected_exceptions = {
        ValueError: rest_exceptions.ValidationError,
        ValidationError: rest_exceptions.ValidationError,
        PermissionError: rest_exceptions.PermissionDenied,
        User.DoesNotExist: rest_exceptions.NotAuthenticated
    }

    def handle_exception(self, exc, context):
        response = exception_handler(exc, context)

        if response is None and isinstance(exc, tuple(self.expected_exceptions.keys())):
            drf_exception_class = self.expected_exceptions[exc.__class__]
            message = str(exc)  # You can customize this part based on your needs

            if issubclass(drf_exception_class, rest_exceptions.ValidationError):
                response_data = {'detail': message}
            else:
                response_data = {'detail': 'An error occurred.'}

            response = Response(response_data, status=drf_exception_class.status_code)

        return response
