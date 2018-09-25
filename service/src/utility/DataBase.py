#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2


class DataBase:
    def __init__(self, property_db):
        self.__property = property_db

    def connect(self):
        return psycopg2.connect(**self.__property.get_dict())
