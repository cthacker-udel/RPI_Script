"""
Represents the basic temperature converter used for converting the read temperature into different formats.
"""

from typing import TypedDict, Callable

class TemperatureConverterFunctions(TypedDict):
    """
    The callback function for converting the supplied temperature reading into celsius.
    """
    celsius: Callable[[int], float]

    """
    The callback function for converting the supplied temperature into kelvin.
    """
    kelvin: Callable[[int], float]

    """
    The callback function for converting the supplied temperature into fahrenheit.
    """
    fahrenheit: Callable[[int], float]


def generate_temp_converter():
    """
    Generates the dictionary for converting temperatures to different formats given the temperature reading from the raspberry pi sensor.

    Returns:
        TemperatureConverterFunctions: Dictionary containing lambdas for converting reading to different formats.
    """
    temperature_dict: TemperatureConverterFunctions = {
        "celsius": lambda reading: reading / 1000.0,
        "fahrenheit": lambda reading: (((reading / 1000.0) * 9.0) / 5.0) + 32.0,
        "kelvin": lambda reading: ((reading / 1000.0) + 273.15)
    }

    return temperature_dict