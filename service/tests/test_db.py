#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from service.src.utility.db.DataBase import DataBase
from service.src.utility.PropertyReader import PropertyReader
from service.src.utility.db.Handler import Handler


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

    def test_handler_execute_query(self):
        db_handler = Handler(self.conn)
        db_version = db_handler.exec('SELECT version()')
        self.assertIsNotNone(db_version, 'Error execute query')

    def test_handler_execute_query_with_param(self):
        db_handler = Handler(self.conn)
        param = ('version()', )
        db_version = db_handler.exec_with_param('SELECT %s', param)
        self.assertIsNotNone(db_version, 'Error execute query')

    def tearDown(self):
        if self.conn is not None:
            self.conn.close()
