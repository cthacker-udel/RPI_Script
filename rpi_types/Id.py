"""
This file defines the schema for the Id type within the RPI ecosystem.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

class Id(declarative_base()):
    """
    Represents the database entry for the registration of a raspberry pi device to gather readings from.
    """
    
    __tablename__ = "ids"
    """
    The name of the table within the SQL database this schema is stored.
    """

    id = Column(Integer, primary_key=True)
    """
    The id PK for the entry.
    """

    pi_id = Column(String(6), unique=True)
    """
    The id assigned to the unique pi.
    """

    name = Column(String(25))
    """
    The name assigned to the PI (the display name).
    """

    created_at = Column(TIMESTAMP)
    """
    Represents the date when the entry was created.
    """

    temperatures = relationship("Temperature", back_populates="pi_id")
    """
    The temperatures linked to this pi instance.
    """