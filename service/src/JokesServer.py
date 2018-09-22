from bottle import route, run


@route('/')
def hello():
    return "Server for jokers"


@route('/api/v1/jokes/<id:int>')
def api_get_jokes_for_id(id):
    return "OK"


if __name__ == '__main__':
    run(host='localhost', port=8787, debug=True)
