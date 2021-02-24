#!/usr/bin/python3
"""
Module for Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Custom amenity class

    Attributes:
        name(str): amenity name

    """
    name = ""
