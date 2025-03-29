import logging
from functools import wraps
from videodb.exceptions import (
    AuthenticationError,
    InvalidRequestError,
    RequestTimeoutError,
    SearchError,
)

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


def handle_videodb_tools_error(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        except AuthenticationError as auth_error:
            return {
                "error": f"Authentication failed. Please check your API key: {auth_error}"
            }
        except InvalidRequestError as invalid_request_error:
            return {
                "error": f"Invalid request. Please verify the input parameters: {invalid_request_error}"
            }
        except RequestTimeoutError as request_timeout_error:
            return {
                "error": f"The request timed out. Please try again later: {request_timeout_error}"
            }
        except SearchError as search_error:
            return {
                "error": f"An error occurred during the search operation: {search_error}"
            }

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

    return wrapper
