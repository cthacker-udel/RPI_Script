"""
Represents the individual temperature readings for respective raspberry pi devices.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

class Temperature(declarative_base()):
    """
    Represents the data stored within the database that stores the raspberry pi temperature reading data.
    """

    __tablename__ = "temperatures"
    """
    The name of the table that contains the temperature data.
    """

    id = Column(Integer, primary_key=True)
    """
    The Id PK for the data entry.
    """
    
    celsius = Column(Float(5), nullable=False)
    """
    The celsius reading for the temperature datum.
    """

    fahrenheit = Column(Float(5), nullable=False)
    """
    The fahrenheit reading for the temperature datum.
    """

    kelvin = Column(Float(5), nullable=False)
    """
    The kelvin reading for the temperature datum.
    """

    pi_id = Column(String(6), ForeignKey("ids.pi_id"), nullable=False)
    """
    The id of the PI this temperature reading belongs to.
    """

    created_at = Column(TIMESTAMP)
    """
    Represents the date when the entry was created.
    """

    pi = relationship("Id", back_populates="temperatures")
    """
    The PI instance this temperature datum belongs to.
    """