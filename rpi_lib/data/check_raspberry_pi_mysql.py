"""
Callback function that receives the raspberry pi id, and checks the mysql database `ids` table for an entry of the raspberry pi.
"""

from typing import Optional
from rpi_constants import color_log, get_database_credentials, generate_pi_id, retry_connection_exp
import os
from dotenv import load_dotenv

def check_raspberry_pi_mysql(debug: Optional[bool] = False, pi_id: Optional[str] = None) -> tuple[Optional[str], bool]:
    """
    Performs an id check in the `ids` table of the `public` schema. Verifying that the raspberry pi exists within the table.

    Args:
        pi_id (Optional[str]): The raspberry pi id to verify within the `ids` table.
        debug (Optional[bool]): Toggle-able debug value for debug logging functionality.

    Returns:
        [str, bool]: [The respective pi id, Whether the raspberry pi exist within the `ids` table]
    """
    log_dict = color_log(debug)
    load_dotenv()

    pi_name = pi_id or os.getenv("PI_NAME")
    ids_table_name = os.getenv("DB_IDS")
    database_credentials = get_database_credentials(None, debug)

    if database_credentials is not None and ids_table_name is not None:
        log_dict["info"](f"Performing id handshake with pi_id {pi_name}")
        database_connection = retry_connection_exp(database_credentials)
        table_cursor = database_connection.cursor(dictionary=True)
        table_cursor.execute(f"SELECT * FROM `{ids_table_name}` WHERE name = %s", (pi_name,))
        found_pi = table_cursor.fetchone()

        if found_pi is None and pi_name is not None:
            generated_pi_id = generate_pi_id()
            log_dict["info"](f"Unable to find raspberry pi `{pi_name}`, inserting respective entry into `ids` table.")
            table_cursor.execute(f"INSERT INTO `{ids_table_name}` (pi_id, name) VALUES (%s, %s)", (generated_pi_id, pi_name))
            database_connection.commit()
            return (generated_pi_id, True)

        found_pi_id: str = str(found_pi.get("pi_id"))
        log_dict["info"](f"Found raspberry pi instance in `{ids_table_name}`.")
        table_cursor.close()
        return (found_pi_id, found_pi is not None)

    log_dict["invalid"]("Database credentials did not load properly, please ensure credentials are correct.")
    return (None, False)