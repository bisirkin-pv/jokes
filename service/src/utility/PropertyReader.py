#!/usr/bin/python
# -*- coding: utf-8 -*-


class PropertyReader:
    """ Class read ini file and create dict """

    def __init__(self, filename):
        self.filename = filename
        self.property = dict()
        self.__read()

    def __read(self):
        try:
            with open(self.filename) as f:
                for line in f:
                    (key, val) = line.split('=')
                    self.property[key] = str(val).replace("\n", "")
        except IOError:
            print("Error create file")

    def get(self, key):
        val = self.property.get(key)
        return val if val is not None else ''

    def get_dict(self):
        return self.property
