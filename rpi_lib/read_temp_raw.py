"""
Defines the helper function for reading the raw temperature output of the raspberry pi's temperature device.    
"""

from rpi_types import TemperatureReading
from rpi_constants import reading_regex, color_log
from typing import Optional
from rpi_constants.enums import TemperatureReadingStatus
from time import time

status_to_enum = {
    "YES": TemperatureReadingStatus.YES,
    "NO": TemperatureReadingStatus.NO
}

def parse_raw_reading(reading: str, debug: Optional[bool] = False) -> Optional[TemperatureReading]:
    """
    Parses the raw temperature reading into the `TemperatureReading` dataclass.

    Args:
        reading (str): The raw temperature reading
        debug (Optional[bool]): Toggle-able boolean value for debug logging functionality.

    Returns:
        Optional[TemperatureReading]: The parsed temperature reading.
    """
    log_dict = color_log(debug)
    parse_result = reading_regex.match(reading)
    if parse_result is None:
        log_dict["invalid"]("Unable to parse raw temperature reading.")
        return None
    
    reading_lsb = parse_result.group("temperaturelsb")
    reading_msb = parse_result.group("temperaturemsb")
    reading_status = parse_result.group("status")

    if (len(reading_lsb) < 1 or reading_lsb is None) or (len(reading_msb) < 1 or reading_msb is None):
        log_dict["invalid"]("Failed parsing named capture groups from temperature reading.")
        return None
    
    parsed_reading = int(f"0x{reading_msb}{reading_lsb}", 16)
    timestamp = time()
    return TemperatureReading(status_to_enum[reading_status], parsed_reading, timestamp)

    

def read_raw_temperature_data(temperature_device_file: str, debug: Optional[bool] = False) -> list[Optional[TemperatureReading]]:
    """
    Reads the raw temperature output from the raspberry pi temperature sensor.
    
    Example output:
    ```py
    [
        "f6 01 4b 46 7f ff 0c 10 5e : crc=5e YES\\n",
        "f6 01 4b 46 7f ff 0c 10 5e t=31437\\n"
    ]
    ```

    Arguments:
        temperature_device_file (str): The file path for the temperature device file.
        debug (Optional[bool]): The toggle-able boolean value for debug logging functionality.
    
    Returns:
        list[str]: [Status of reading, datum]
    """
    log_dict = color_log(debug)
    temperature_readings: list[Optional[TemperatureReading]] = []
    with open(temperature_device_file, "r", encoding="utf-8") as temperature_device:
        reading = temperature_device.readlines()
        i = 0
        while i < len(reading):
            reading_with_status = reading[i]
            log_dict["info"](f"Parsing temperature {reading_with_status}")
            temperature_readings.append(parse_raw_reading(reading_with_status, debug))
            i += 2
    return temperature_readings


