"""
Helper function for converting the read temperature data to json-compliant values.
"""

from rpi_types.dto import TemperatureDTO
from dataclasses import asdict
from typing import Any
import json

def convert_temperature_data(read_temperature_data: list[TemperatureDTO]) -> str:
    """
    Converts the given temperature data into json-compliant string.

    Args:
        read_temperature_data (list[TemperatureDTO]): The read temperature data from the raspberry pi temperature sensor.

    Returns:
        str: The encoded temperature data array.
    """
    converted_temp_data: list[dict[str, Any]] = []
    for each_temperature_datum in read_temperature_data:
        converted_temp_data.append(asdict(each_temperature_datum))
    encoded_array = json.dumps(converted_temp_data)
    return encoded_array