"""
Helper function for performing a "handshake" with the database to ensure the raspberry pi is registered in the `ids` table before proceeding with propagating temperature data to the `temperatures` database.
"""

import os
from dotenv import load_dotenv
from rpi_constants.color_log import color_log
from typing import Callable, Optional

def handshake_ids(check_id: Callable[[Optional[str]], bool]) -> bool:
    """
    Performs a "handshake" with the remote database table `ids` to ensure that the raspberry pi is registered within the database.

    Args:
        check_id (Callable[[Optional[str]], bool]): The callback function that receives the raspberry pi id (name). Performs an id handshake given the raspberry pi id.

    Returns:
        bool: Whether the raspberry pi exists within the `ids` table.
    """
    log_dict = color_log()
    load_dotenv()

    pi_name = os.getenv("PI_NAME")
    does_pi_exist = check_id(pi_name)

    if does_pi_exist:
        log_dict["info"](f"Verified that raspberry pi with id {pi_name} exists in the `ids` database.")
        return True
    
    log_dict["invalid"](f"Raspberry Pi with name {pi_name} does NOT exist in the `ids` table.")
    return False