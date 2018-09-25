#!/usr/bin/python
# -*- coding: utf-8 -*-


class Handler:
    """ Work with query """

    def __init__(self, connection):
        self.__connection = connection

    """ Execute simple query, return one row """
    def exec(self, query):
        cur = self.__connection.cursor()
        cur.execute(query)
        result = cur.fetchone()
        return result
