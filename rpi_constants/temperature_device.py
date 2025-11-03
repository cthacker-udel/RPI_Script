"""
Contains all the constant strings related to the temperature device within the raspberry pi device.
"""
import glob
from rpi_constants.color_log import color_log
from typing import Optional
from rpi_constants.simulation.simulation_constants import simulation_folder_name
from rpi_constants.simulation.create_mock_temp_sensor import create_mock_temp_sensor

"""
Defines the general base directory where the temperature device exists.
"""
temperature_device_base_dir = "/sys/bus/w1/devices"


"""
Represents the callback used for fetching the base directory of the temperature device.
"""
def get_temperature_device_folder(base_dir: str, simulate: Optional[bool] = False, debug: Optional[bool] = False) -> str:
    """
    Callback function that generates and returns the temperature device folder path.

    Args:
        base_dir (str): Represents the base directory to search for the temperature device within.
        simulate (Optional[bool]): Represents the toggle-able boolean for simulating temperature data.
        debug (Optional[bool]): Represent the toggle-able boolean for debug logging functionality.

    Returns:
        str: The path to the temperature device's folder.
    """
    log_dict = color_log(debug)

    if simulate:
        return simulation_folder_name

    if len(base_dir) == 0:
        log_dict["invalid"]("Supplied empty base directory, terminating.")
        return ""
    
    glob_str = f"{base_dir}28*"
    glob_result = glob.glob(glob_str)

    if len(glob_result) < 1:
        log_dict["invalid"](f"Cannot find temperature device using the glob pattern {glob_str}")
        return ""
    
    first_found_folder = glob_result[0]
    return first_found_folder

"""
Represents the callback to fetch the file containing the temperature device.    
"""
def get_temperature_device_file(folder_path: str, simulate: Optional[bool] = False, simulation_sensor_filename: Optional[str] = None, debug: Optional[bool] = False) -> str:
    """
    Fetches the singular file that contains the temperature device readings.

    Args:
        folder_path (str): Represents the path to the temperature device's folder.
        simulate (Optional[bool]): Represents the toggle-able boolean value for simulating temperature data.
        simulation_sensor_filename (Optional[str]): Represents the filename for the simulation temperature sensor.
        debug (Optional[bool]): Represents the toggle-able boolean value for debug logging functionality.

    Returns:
        str: The found temperature device file.
    """
    log_dict = color_log(debug)

    if simulate:
        return create_mock_temp_sensor(simulation_sensor_filename)

    if len(folder_path) < 1:
        log_dict["invalid"]("Supplied empty folder path for temperature device.")
        return ""
    
    found_file = f"{folder_path}/w1_slave"
    return found_file

"""
Represents the callback to fetch the path to the temperature device within the raspberry pi.
"""
def get_temperature_device_path(simulate: Optional[bool] = False, simulation_sensor_filename: Optional[str] = None, debug: Optional[bool] = False) -> str:
    """
    Returns the path to the temperature device within the raspberry pi.

    Returns:
        str: The path to the temperature device within the raspberry pi.
    """
    return get_temperature_device_file(get_temperature_device_folder(temperature_device_base_dir, simulate, debug), simulate, simulation_sensor_filename, debug)