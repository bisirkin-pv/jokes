#!/usr/bin/python
# -*- coding: utf-8 -*-
from bottle import route, run
from service.src.utility.db.DataBase import DataBase
from service.src.utility.PropertyReader import PropertyReader
from service.src.utility.db.Handler import Handler
import argparse
import sys


def create_parser():
    __parser = argparse.ArgumentParser()
    __parser.add_argument('-db', '--db_setting', default="../../dbSettingPostgres.ini")
    return __parser


@route('/')
def hello():
    return "Server for jokers"


@route('/api/v1/jokes/<id:int>')
def api_get_jokes_for_id(id):
    db = DataBase(PropertyReader(namespace.db_setting))
    conn = db.connect()
    db_handler = Handler(conn)
    jokes = db_handler.exec_with_param('SELECT txt FROM dbo.jokes WHERE id = %s', (id,))
    return jokes[0].replace("\n", " ") if jokes is not None else ''


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    run(host='localhost', port=8787, debug=True)
