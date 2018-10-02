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

    """ Execute simple query, return one row """
    def exec_with_param(self, query, *args):
        cur = self.__connection.cursor()
        cur.execute(query, args)
        result = cur.fetchone()
        return result
