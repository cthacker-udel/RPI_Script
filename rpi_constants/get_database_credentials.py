"""
Defines the helper function to fetch database credentials from the environment.
"""

from dotenv import load_dotenv
import os
from rpi_types import DatabaseCredentials
from typing import Optional
from rpi_constants.color_log import color_log

DB_USERNAME_ENVIRONMENT_KEY = "DB_USERNAME"
DB_PASSWORD_ENVIRONMENT_KEY = "DB_PASSWORD"
DB_HOST_ENVIRONMENT_KEY = "DB_HOST"
DB_ENVIRONMENT_KEY = "DB"

def get_database_credentials(schema_name: Optional[str] = None, debug: Optional[bool] = False) -> Optional[DatabaseCredentials]:
    """
    Fetches the database credentials from the environment variables stored in the raspberry pi.

    Arguments:
        schema_name (Optional[str]): Represents the optional schema name which allows for dynamic database entry.
        debug (Optional[bool]): Toggle-able boolean value for debug logging functionality.

    Returns:
        Optional[DatabaseCredentials]: The stored database credentials within the raspberry pi device.
    """
    log_dict = color_log(debug)
    load_dotenv()

    log_dict["info"]("Accessing stored database credentials")
    username = os.getenv(DB_USERNAME_ENVIRONMENT_KEY)
    password = os.getenv(DB_PASSWORD_ENVIRONMENT_KEY) or ""
    database_host = os.getenv(DB_HOST_ENVIRONMENT_KEY)
    database_schema = schema_name or os.getenv(DB_ENVIRONMENT_KEY)

    if username is None or database_host is None or database_schema is None:
        log_dict["invalid"]("Credentials supplied are invalid or do not exist, check the values or ensure they exist.")
        return None

    return DatabaseCredentials(username, password, database_host, database_schema)
    