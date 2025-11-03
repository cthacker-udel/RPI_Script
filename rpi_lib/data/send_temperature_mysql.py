"""
Defines the callback for sending data to the remote MariaDB database using the credentials supplied as environment variables.
"""

from mysql.connector import connect
from rpi_types.dto import TemperatureDTO
from rpi_constants import get_database_credentials, color_log
import os

def send_temperature_mysql(temperature_data: TemperatureDTO) -> bool:
    log_dict = color_log()
    database_credentials = get_database_credentials()
    temperature_table = os.getenv("DB_TEMPERATURES")

    if database_credentials is not None and temperature_table is not None:
        log_dict["info"]("Connecting to database to send temperature data reading.")
        database_connection = connect(
            host=database_credentials.host,
            user=database_credentials.user,
            password=database_credentials.password,
            database=database_credentials.schema
        )

        table_cursor = database_connection.cursor(dictionary=True)
        table_cursor.execute(f"INSERT INTO `{temperature_table}` (celsius, fahrenheit, kelvin, pi_id) VALUES (%s, %s, %s, %s)", (temperature_data.celsius, temperature_data.fahrenheit, temperature_data.kelvin, temperature_data.pi_id))
        database_connection.commit()
        table_cursor.close()

        return True

    return False