#!/usr/bin/python3
"""Basemodel module for other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""

    forma = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """intializer"""
        if kwargs:
            kwargs["created_at"] = \
                    datetime.strptime(kwargs["created_at"], __class__.forma)
            kwargs["updated_at"] = \
                datetime.strptime(kwargs["updated_at"], __class__.forma)

            for key in kwargs.keys():
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save and update the update_at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ to_dict definition """
        
        dic = {}
        for key, item in self.__dict__.items():
            if key not in ['created_at', 'updated_at']:
                dic[key] = item

        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
