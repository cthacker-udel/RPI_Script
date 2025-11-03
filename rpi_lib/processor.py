"""
Represents the general processor for the raspberry pi's temperature data.    
"""

from rpi_lib import read_raw_temperature_data
from rpi_constants import get_temperature_device_path
from rpi_constants import color_log, generate_temp_converter
from rpi_constants.enums import TemperatureReadingStatus
from rpi_types.dto import TemperatureDTO
from typing import Optional
from rpi_constants.simulation import upload_mock_data
import os


def processor(pi_id: str, simulate: Optional[bool] = False, simulate_sensor_filename: Optional[str] = None) -> list[TemperatureDTO]:
    """
    Processes the readings from the raspberry pi and converts into DTO dataclasses.

    Args:
        pi_id (str): The id belonging to the raspberry pi, used for propagating the temperature readings to the remote database.
        simulate (Optional[bool]): Represents whether the run environment of the script constitutes simulation behavior.
        simulate_sensor_filename (Optional[str]): Represents the temperature sensor simulator filename.

    Returns:
        list[TemperatureDTO]: The read temperature data prepared for propagation to the server.
    """
    log_dict = color_log()

    if not simulate and "PI_NAME" not in os.environ:
        log_dict["invalid"]("Environment variable PI_NAME does not exist. Please ensure PI has a display name.")
        exit(0)
    
    log_dict["info"]("Gathering path for temperature sensor")
    temperature_device_path = get_temperature_device_path(simulate, simulate_sensor_filename)

    if simulate:
        upload_mock_data(temperature_device_path)

    log_dict["info"]("Reading raw temperature data")
    found_temperatures = read_raw_temperature_data(temperature_device_path)

    if len(found_temperatures) == 0:
        log_dict["invalid"]("Could not read any temperatures, terminating")
        return []

    ind = 0
    compiled_readings: list[TemperatureDTO] = []
    for each_temperature_data in found_temperatures:
        if each_temperature_data is None:
            log_dict["invalid"](f"Temperature data at index {ind} is `None`")
        else:
            each_temperature_status = each_temperature_data.status
            each_temperature_reading = each_temperature_data.temperature
            each_temperature_timestamp = each_temperature_data.timestamp

            if each_temperature_status == TemperatureReadingStatus.YES:
                temp_converter = generate_temp_converter()
                reading_fahrenheit = temp_converter["fahrenheit"](each_temperature_reading)
                reading_celsius = temp_converter["celsius"](each_temperature_reading)
                reading_kelvin = temp_converter["kelvin"](each_temperature_reading)
                converted_reading = TemperatureDTO(reading_celsius, reading_fahrenheit, reading_kelvin, each_temperature_timestamp, pi_id)
                compiled_readings.append(converted_reading)
        ind += 1

    return compiled_readings


