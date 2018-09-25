#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from service.src.utility.db.DataBase import DataBase
from service.src.utility.PropertyReader import PropertyReader


class TestDatabase(unittest.TestCase):
    def setUp(self):
        db = DataBase(PropertyReader("../../dbSettingPostgres.ini"))
        self.conn = db.connect()

    def test_connect(self):
        self.assertIsNotNone(self.conn, 'Error connecting to database')

    def test_request(self):
        cur = self.conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        self.assertIsNotNone(db_version, 'Error execute query')

    def tearDown(self):
        if self.conn is not None:
            self.conn.close()
