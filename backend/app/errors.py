from app.schemas import ErrorResponse


class ApiException(Exception):
    """ Exception that was caused during API operation """

    def __init__(self, status_code: int, error_code: int, description: str):
        self.status_code = status_code
        self.error_code = error_code
        self.description = description
    
    def get_response(self):
        return ErrorResponse(
            code=self.error_code,
            description=self.description
        )


class UnexpectedError(ApiException):
    def __init__(self):
        super().__init__(500, 0, 'Unexpected error')


class InvalidInputFormatError(ApiException):
    def __init__(self):
        super().__init__(400, 1, 'Invalid input format')


class AuthorizationRequiredError(ApiException):
    def __init__(self):
        super().__init__(401, 2, 'Authorization required')


class AccessDeniedError(ApiException):
    def __init__(self):
        super().__init__(403, 3, 'Access is denied')


class NotFoundError(ApiException):
    def __init__(self):
        super().__init__(404, 4, 'Content was not found')


class InvalidAccessTokenError(ApiException):
    def __init__(self):
        super().__init__(400, 5, 'Invalid access token')


class InvalidAuthDataError(ApiException):
    def __init__(self):
        super().__init__(400, 6, 'Invalid login or password')


class InvalidRefreshTokenError(ApiException):
    def __init__(self):
        super().__init__(400, 7, 'Invalid refresh token')


class UnconfirmedEmailError(ApiException):
    def __init__(self):
        super().__init__(400, 8, 'User profile is not confirmed by E-Mail')


class TakenLoginError(ApiException):
    def __init__(self):
        super().__init__(400, 9, 'User with such login already exist')


class InvalidConfirmationCodeError(ApiException):
    def __init__(self):
        super().__init__(400, 10, 'Invalid confirmation code')


class InvalidMessageTimestampError(ApiException):
    def __init__(self):
        super().__init__(400, 11, 'User with such login already exist')


class InterlocutorNotFoundError(ApiException):
    def __init__(self):
        super().__init__(500, 12, 'Interlocutor for random chat wasn\'t found')
