"""
Contains all the constant strings related to the temperature device within the raspberry pi device.
"""
import glob

"""
Defines the general base directory where the temperature device exists.
"""
temperature_device_base_dir = "/sys/bus/w1/devices"


"""
Represents the callback used for fetching the base directory of the temperature device.
"""
def get_temperature_device_folder(base_dir: str) -> str:
    """
    Callback function that generates and returns the temperature device folder path.

    Args:
        base_dir (str): Represents the base directory to search for the temperature device within.

    Returns:
        str: The path to the temperature device's folder.
    """
    if len(base_dir) == 0:
        return ""
    
    glob_str = f"{base_dir}28*"
    glob_result = glob.glob(glob_str)

    if len(glob_result) < 1:
        return ""
    
    first_found_folder = glob_result[0]
    return first_found_folder

"""
Represents the callback to fetch the file containing the temperature device.    
"""
def get_temperature_device_file(folder_path: str) -> str:
    """
    Fetches the singular file that contains the temperature device readings.

    Args:
        folder_path (str): Represents the path to the temperature device's folder.

    Returns:
        str: The found temperature device file.
    """
    if len(folder_path) < 1:
        return ""
    
    found_file = f"{folder_path}/w1_slave"
    return found_file