"""
Represents the helper function for propagating the temperature data to the external database. Requires a direct connection to the database.
"""

from rpi_types.dto import TemperatureDTO
from typing import Callable
from rpi_constants import color_log

def send_temperature_data(bulk_temperature_data: list[TemperatureDTO], send_data: Callable[[TemperatureDTO], bool]) -> None:
    log_dict = color_log()

    for each_temperature_data in bulk_temperature_data:
        log_dict['info'](f"Sending data {each_temperature_data} to database.")
        try: 
            sent_data = send_data(each_temperature_data)

            if sent_data:
                log_dict['info']("Successfully sent temperate data to database.")
            else:
                log_dict["invalid"]("Failed to send temperature data to database.")
        except Exception as e:
            print('e = ', e)
            log_dict['invalid'](f"Failed to send temperature data {each_temperature_data}")
    
