"""
Defines the database credentials used internally within the raspberry pi for uploading temperatures.
"""

from dataclasses import dataclass

@dataclass
class DatabaseCredentials:
    """
    Represents the schema for database credentials throughout the application.
    """

    user: str
    """
    The username for authentication.
    """

    password: str
    """
    The password for authentication.
    """

    host: str
    """
    The hostname for the database.
    """

    schema: str
    """
    The schema accessed.
    """