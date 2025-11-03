"""
Constant regex expression for parsing the temperature data from the stringified raspberry pi temperature reading.    
"""
import re

reading_regex = re.compile("^(?P<temperaturelsb>[0-9a-f][0-9a-f]) (?P<temperaturemsb>[0-9a-f][0-9a-f]) [ a-f0-9]+: crc=[0-9a-f][0-9a-f] (?P<status>[a-zA-Z]+)", re.MULTILINE)