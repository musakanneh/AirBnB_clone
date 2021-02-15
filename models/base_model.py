#!/usr/bin/python3
"""Custombase class for the entire project"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Custom base model class"""

    def __init__(self, *args, **kwargs):
        """Public instance artributes

        Args:
            *args(args): input arguments
            **kwargs(kwargs): input arguments

        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    date = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, date)
                elif key[0] == "_":
                    setattr(self, key, value)

    def __str__(self):
        """Public instance method"""
        pass
