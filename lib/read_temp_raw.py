"""
Defines the helper function for reading the raw temperature output of the raspberry pi's temperature device.    
"""

def parse_raw_reading(reading: str) -> 

def read_temp_raw(temperature_device_file: str) -> list[str]:
    """
    Reads the raw temperature output from the raspberry pi temperature sensor.
    
    Example output:
    ```py
    [
        "f6 01 4b 46 7f ff 0c 10 5e : crc=5e YES\\n",
        "f6 01 4b 46 7f ff 0c 10 5e t=31437\\n"
    ]
    ```
    
    Returns:
        list[str]: [Status of reading, datum]
    """
    temperature_readings = []
    with open(temperature_device_file, "r", encoding="utf-8") as temperature_device:
        reading = temperature_device.readlines()
        i = 0
        while i < len(reading):
            reading_with_status = reading[i]
            i += 2


