"""
Represents a local temperature reading internally within the raspberry pi device.    
"""

from dataclasses import dataclass
from rpi_constants.enums import TemperatureReadingStatus

@dataclass
class TemperatureReading:
    """
    Represents the local temperature reading directly from the raspberry pi device.
    """
    
    status: TemperatureReadingStatus
    """
    The status of the temperature reading.
    """

    temperature: int
    """
    The raw temperature value.
    """

    timestamp: float
    """
    The raw timestamp associated with the data reading.
    """