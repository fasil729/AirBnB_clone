#!/usr/bin/python3
"""Basemodel module for other classes"""


import uuid
from datetime import datetime


class BaseModel:
    """defines all common attributes/methods for other classes"""

    forma = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """intializer"""
        if kwargs:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"], __class__.forma)
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"], __class__.forma)
            for key in kwargs.keys():
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save and update the update_at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """changes the pbject format to dictionary format"""
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
