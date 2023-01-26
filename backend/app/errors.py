from enum import Enum

from pydantic.dataclasses import dataclass

from schemas import ErrorResponse


@dataclass
class ApiError:
    status_code: int
    error_code: int
    description: str
    
    def get_response(self) -> ErrorResponse:
        return ErrorResponse(code=self.error_code, description=self.description)


class ApiException(Exception):
    """ Exception that was caused during API operation """
    def __init__(self, error: ApiError):
        self.error = error


class ApiErrorType(ApiError, Enum):
    UNEXPECTED_ERROR = ApiError(
        status_code=500,
        error_code=0,
        description='Unexpected error'
    )
    INVALID_INPUT_FORMAT = ApiError(
        status_code=400,
        error_code=1,
        description='Invalid input format'
    )
    AUTHORIZATION_REQUIRED = ApiError(
        status_code=401,
        error_code=2,
        description='Authorization required'
    )
    ACCESS_DENIED = ApiError(
        status_Code=403,
        error_code=3,
        description='Access is denied'
    )
    NOT_FOUND = ApiError(
        status_code=404,
        error_code=4,
        description='Content was not found'
    )
    INVALID_ACCESS_TOKEN = ApiError(
        status_Code=400,
        error_code=5,
        description='Invalid access token'
    )
    INVALID_AUTH_DATA = ApiError(
        status_code=404,
        error_code=6,
        description='Invalid login or password'
    )
    INVALID_REFRESH_TOKEN = ApiError(
        status_code=400,
        error_code=7,
        description='Invalid refresh token'
    )
    UNCONFIRMED_EMAIL = ApiError(
        status_code=400,
        error_code=8,
        description='User profile is not confirmed by E-Mail'
    )
    LOGIN_ALREADY_TAKEN = ApiError(
        status_code=400,
        error_code=9,
        description='User with such login already exist'
    )
    INVALID_CONFIRMATION_CODE = ApiError(
        status_code=400,
        error_code=10,
        description='Invalid confirmation code'
    )
    RATED_PROFILE = ApiError(
        status_code=400,
        error_code=11,
        description='This profile was already rated'
    )
    INVALID_MSG_TIMESTAMP = ApiError(
        status_code=400,
        error_code=12,
        description='Invalid timestamp in the message'
    )
    NO_INTERLOCUTOR_FOUND = ApiError(
        status_code=500,
        error_code=13,
        description="Interlocutor for random chat wasn't found"
    )
