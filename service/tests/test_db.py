#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from service.src.utility.DataBase import DataBase
from service.src.utility.PropertyReader import PropertyReader


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = None

    def test_connect(self):
        db = DataBase(PropertyReader("../../dbSettingPostgres.ini"))
        self.conn = db.connect()
        self.assertIsNotNone(self.conn, 'Error connecting to database')

    def tearDown(self):
        if self.conn is not None:
            self.conn.close()
