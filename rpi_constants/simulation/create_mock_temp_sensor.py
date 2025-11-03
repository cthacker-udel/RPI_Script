"""
Helper function for creating the mock temperature sensor file.
"""

import os
from rpi_constants.simulation.simulation_constants import simulation_folder_name, simulation_temperature_sensor, simulation_root_marker_file
from typing import Optional
from rpi_constants.color_log import color_log
from rpi_constants.simulation.find_root_path import find_root_path

def create_mock_temp_sensor(file_name: Optional[str]) -> str:
    """
    Creates the mock temperature sensor if the mock temperature sensor file does not exist.

    Args:
        file_name (str): The name of the mock temperature sensor file.

    Returns:
        str: The file path for the mock temperature sensor.
    """
    log_dict = color_log()

    root_path = find_root_path(simulation_root_marker_file)
    temperature_sensor_path = f"{root_path}\\{simulation_folder_name}\\{simulation_temperature_sensor if file_name is None else file_name}" 
    
    if not os.path.exists(temperature_sensor_path):
        log_dict["info"](f"Creating temperature sensor file with path {temperature_sensor_path}")
        os.makedirs(f"{root_path}\\{simulation_folder_name}")
        with open(temperature_sensor_path, "w", encoding="utf-8") as temperature_sensor_file:
            temperature_sensor_file.write("")
        
    return temperature_sensor_path

