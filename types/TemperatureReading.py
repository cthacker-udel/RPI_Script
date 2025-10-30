"""
Represents a local temperature reading internally within the raspberry pi device.    
"""

from dataclasses import dataclass

@dataclass
class TemperatureReading:
    status: str
    reading: list[int]