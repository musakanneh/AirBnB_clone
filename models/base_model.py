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
        """String method for base class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime

        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Method returns a dictionary containing all 
        keys/values of __dict__ instance

        """
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = datetime.isoformat(self.created_at)
        my_dict['updated_at'] = datetime.isoformat(self.updated_at)
        return my_dict
