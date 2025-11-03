"""
Represents the helper function for propagating the temperature data to the external database. Requires a direct connection to the database.
"""

from rpi_types.dto import TemperatureDTO
from typing import Callable, Optional
from rpi_constants import color_log

def send_temperature_data(bulk_temperature_data: list[TemperatureDTO], send_data: Callable[[TemperatureDTO, Optional[bool]], bool], debug: Optional[bool] = False) -> None:
    """
    Sends the gathered temperature data from the internal temperature device to the remote database.

    Args:
        bulk_temperature_data (list[TemperatureDTO]): The array of gathered temperature data.
        send_data (Callable[[TemperatureDTO], bool]): The callback that takes the gathered temperature data, and returns whether the data was propagated properly.
        debug (Optional[bool], optional): Toggle-able boolean value for debug logging functionality. Defaults to False.
    """
    log_dict = color_log(debug)

    for each_temperature_data in bulk_temperature_data:
        log_dict['info'](f"Sending data {each_temperature_data} to database.")
        try: 
            sent_data = send_data(each_temperature_data, debug)

            if sent_data:
                log_dict['info']("Successfully sent temperate data to database.")
            else:
                log_dict["invalid"]("Failed to send temperature data to database.")
        except:
            log_dict['invalid'](f"Failed to send temperature data {each_temperature_data}")
    
