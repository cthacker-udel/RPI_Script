"""
Helper function for establishing a mysql connection with retry parameters.
"""

from typing import Optional, Union
from rpi_types import DatabaseCredentials
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector import connect
from rpi_constants import color_log
import time

def retry_connection_exp(database_credentials: DatabaseCredentials, retry_count: Optional[int] = 5, base_delay_seconds: Optional[int] = 1) -> Union[PooledMySQLConnection, MySQLConnectionAbstract]:
    """
    Retries connecting to the remote database with exponential backoff to delay retries.

    Args:
        database_credentials (DatabaseCredentials): The credentials used for connecting to the remote database.
        retry_count (Optional[int], optional): Defines the default # of attempts to connect to the remote database. Defaults to 5.
        base_delay_seconds (Optional[int], optional): Defines the # of seconds to apply to the exponential backoff formula. Defaults to 1.

    Raises:
        Exception: If the max # of attempts are used for connecting to the remote database.
        Exception: If the resultant database connection equals `None`.

    Returns:
        Union[PooledMySQLConnection, MySQLConnectionAbstract]: The database connection.
    """
    log_dict = color_log()
    retry_connection_amount = retry_count or 5
    database_connection: Optional[Union[PooledMySQLConnection, MySQLConnectionAbstract]] = None

    for attempt in range(1, retry_connection_amount + 1):
        try:
            log_dict['info'](f"Database connection attempt #{attempt}")
            database_connection = connect(host=database_credentials.host, user=database_credentials.user, password=database_credentials.password, database=database_credentials.schema)
            log_dict['info']("Successfully connected!")
            break
        except:
            if attempt == retry_count:
                raise Exception(f"Failed to connect to the database after {retry_connection_amount} attempts")
            delay = base_delay_seconds * (2 ** (attempt - 1))
            log_dict['info'](f"Attempt {attempt} failed, retrying in {delay} seconds...")
            time.sleep(delay)

    if database_connection is None:
        raise Exception("Database connection is invalid, terminating.")

    return database_connection
