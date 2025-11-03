"""
Helper function for uploading mock temperature data to the mock temperature sensor file.
"""

from rpi_constants.color_log import color_log
import random

def upload_mock_data(file_path: str) -> list[str]:
    """
    Creates + uploads mock temperature data to the mock temperature sensor file.

    Args:
        file_path (str): The path to the mock temperature sensor.

    Returns:
        list[str]: The mock temperature data uploaded.
    """
    log_dict = color_log()

    log_dict['info']("Generating random temperature")
    random_celsius_temperature = round(random.uniform(10.0, 35.0))
    temperature_raw = (random_celsius_temperature * 16) & 0xFFFF
    temperature_msb = (temperature_raw >> 8) & 0xFF
    temperature_lsb = temperature_raw & 0xFF
    log_dict["info"](f"Generated random temperature {random_celsius_temperature}")

    other_random_bytes = [random.randint(0, 255) for _ in range(6)]
    mock_temperature_data = f"{hex(temperature_lsb)[2:].zfill(2)} {hex(temperature_msb)[2:].zfill(2)} {' '.join([hex(x)[2:].zfill(2) for x in other_random_bytes])}"
    mock_temperature_crc = f"{mock_temperature_data} : crc=5e YES\n"
    mock_temperature_reading = f"{mock_temperature_data} t={temperature_raw}\n"
    log_dict['info']("Crafted mock temperature data, uploading to mock temperature sensor")

    with open(file_path, "w") as mock_temperature_sensor_file:
        mock_temperature_sensor_file.write(mock_temperature_crc)
        mock_temperature_sensor_file.write(mock_temperature_reading)
        log_dict["info"]("Wrote mock data to random temperature sensor file.")

    return [mock_temperature_crc, mock_temperature_reading]


