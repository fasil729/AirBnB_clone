#!/usr/bin/python3
"""intilizer module"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
storage = FileStorage()
storage.reload()
