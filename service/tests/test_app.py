#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from service.src.utility.db.DataBase import DataBase
from service.src.utility.PropertyReader import PropertyReader
from service.src.JokesServer import api_get_jokes_for_id


class TestApp(unittest.TestCase):
    """ Test application methods"""

    def setUp(self):
        db = DataBase(PropertyReader("../../dbSettingPostgres.ini"))
        self.conn = db.connect()

    def test_api_get_jokes_for_id(self):
        result = api_get_jokes_for_id(1)
        self.assertIsNotNone(result, 'Error method "api_get_jokes_for_id" not return data')

    def test_api_get_jokes_for_id_not_found(self):
        result = api_get_jokes_for_id(-1)
        self.assertEquals(result, '')

    def tearDown(self):
        if self.conn is not None:
            self.conn.close()