#!/usr/bin/python3
"""
Test suits for base model
"""

import os
import re
import json
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests attributes of the base model"""

    def test_basic(self):
        """Tests basic imputs for the BaseModel class"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.number = 89
        self.assertEqual(
                [my_model.name, my_model.number], ["ALX", 89])

    def test_init(self):
        """Tests if created_at, update_at and id exists"""
        test_init_model = BaseModel
        self.assertTrue(hasattr(test_init_model, "id"))
        self.assertTrue(hasattr(test_init_model, "updated_at"))
        self.assertTrue(hasattr(test_init_model, "created_at"))


if __name__ == '__main__':
    unittest.main()
