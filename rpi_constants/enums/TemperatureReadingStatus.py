"""
Represents the enum value for the TemperatureReading's status. Can be a YES or NO value.
"""

from enum import Enum

"""
Represents the enum value of the temperature reading's status.
"""
class TemperatureReadingStatus(Enum):
    """
    Represents the YES status of the temperature reading. Occurs when the temperature reading is successful.
    """
    YES = 0

    """
    Represents the NO status of the temperature reading. Occurs when the temperature reading fails.
    """
    NO = 1