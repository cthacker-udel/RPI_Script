"""
Represents the individual temperature readings for respective raspberry pi devices.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Temperature(declarative_base()):
    """
    The name of the table that contains the temperature data.
    """
    __tablename__ = "temperatures"

    """
    The Id PK for the data entry.
    """
    id = Column(Integer, primary_key=True)
    
    """
    The celsius reading for the temperature datum.
    """
    celsius = Column(Float(5), nullable=False)

    """
    The fahrenheit reading for the temperature datum.
    """
    fahrenheit = Column(Float(5), nullable=False)

    """
    The kelvin reading for the temperature datum.
    """
    kelvin = Column(Float(5), nullable=False)

    """
    The timestamp corresponding to the temperature datum.
    """
    temperature_timestamp = Column(Integer(), nullable=False)

    """
    The id of the PI this temperature reading belongs to.
    """
    pi_id = Column(String(6), ForeignKey("ids.pi_id"))

    """
    The PI instance this temperature datum belongs to.
    """
    pi = relationship("Id", back_populates="temperatures")
