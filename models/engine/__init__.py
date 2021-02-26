#!/bin/usr/python3
"""
Init for models module
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
