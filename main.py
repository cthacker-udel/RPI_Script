#!/usr/bin/env python3
"""
The entry file for the raspberry pi project. Handles the command line arguments sent to the script.    
"""

import argparse
import time
from rpi_constants import color_log, convert_temperature_data
from rpi_lib import processor, send_temperature_data
from rpi_lib.data import send_temperature_mysql, check_raspberry_pi_mysql
import urllib.request
from typing import Optional

###############################
## INITIALIZING CLI SCHEMA
###############################
parser = argparse.ArgumentParser(description="Run the raspberry pi temperature input/output script.")
parser.add_argument("-delay", "--delay", type=int, help="The delay in seconds to apply to the temperature reading and output operations.", nargs="?", const=1)
parser.add_argument("-url", "--url", type=str, help="The external URL receiving the temperature data.")
parser.add_argument("-simulate", "--simulate", action="store_true", help="Use fake temperature data to simulate a raspberry pi, useful for testing externally.")
parser.add_argument("-simulate_sensor_filename", "--simulate_sensor_filename", type=str, help="The mock temperature sensor filename, defaults to simulation_sensor", nargs="?")
parser.add_argument("-debug", "--debug", action="store_true", help="Toggles debug logging while the process runs.")

###############################
## PARSING CLI ARGS
###############################
cmd_line_arguments = parser.parse_args()
export_delay: int = cmd_line_arguments.delay or 1
external_url: Optional[str] = cmd_line_arguments.url
simulate_data: Optional[bool] = cmd_line_arguments.simulate
simulate_sensor_filename: Optional[str] = cmd_line_arguments.simulate_sensor_filename
debug: Optional[bool] = cmd_line_arguments.debug

def main():

    [pi_id, does_pi_exist] = check_raspberry_pi_mysql(debug)
    while does_pi_exist and pi_id is not None:
        log_dict = color_log(debug)
        log_dict["info"]("Gathering temperature data.")
        read_temperature_data = processor(pi_id, simulate_data, simulate_sensor_filename, debug)
        log_dict["info"]("Processed temperature data, propagating processed temperature readings to database.")
        send_temperature_data(read_temperature_data, send_temperature_mysql, debug)

        if external_url is not None and len(external_url):
            log_dict["info"](f"Exporting data to external url: {external_url}")
            converted_data = convert_temperature_data(read_temperature_data) 
            urllib.request.Request(external_url, data=converted_data.encode("utf-8"), method="POST")

        time.sleep(export_delay)
 

if __name__ == "__main__":
    main()