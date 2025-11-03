"""
Represents the DTO for the acquired temperature reading from the raspberry pi.
"""

from typing import Self
from dataclasses import dataclass
from datetime import datetime

@dataclass
class TemperatureDTO:
    """
    Represents the data-transfer object (DTO) for the temperature reading.
    """

    celsius: float
    """
    The celsius of the temperature reading.
    """

    fahrenheit: float
    """
    The fahrenheit of the temperature reading.
    """

    kelvin: float
    """
    The kelvin of the temperature reading.
    """

    timestamp: float
    """
    The timestamp of the temperature reading.
    """

    pi_id: str
    """
    The id of the raspberry pi device that the temperature reading sources from.
    """

    def __str__(self: Self) -> str:
        """
        Overrides the internal `toString` or `string` implementation with a custom-made implementation.

        Args:
            self (Self): The stringified class instance.

        Returns:
            str: The overridden `string` implementation for the class.
        """
        return f"{datetime.fromtimestamp(self.timestamp)}: {self.celsius}\u00b0C {self.fahrenheit}\u00b0F {self.kelvin}\u00b0K"