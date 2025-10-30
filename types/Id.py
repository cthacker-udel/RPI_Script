"""
This file defines the schema for the Id type within the RPI ecosystem.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class Id(declarative_base()):
    """
    The name of the table within the SQL database this schema is stored.
    """
    __tablename__ = "ids"

    """
    The id PK for the entry.
    """
    id = Column(Integer, primary_key=True)

    """
    The id assigned to the unique pi.
    """
    pi_id = Column(String(6), unique=True)

    """
    The name assigned to the PI (the display name).
    """
    name = Column(String(10))

    """
    The temperatures linked to this pi instance.
    """
    temperatures = relationship("Temperature", back_populates="pi")