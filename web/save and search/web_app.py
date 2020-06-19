from pathlib import Path
from urllib.parse import parse_qs
from typing import Callable, Iterable
from wsgiref.simple_server import make_server
import json


class HTTPError(Exception):

    def __init__(self, reason: str, code: int):
        self.code = code
        self.reason = reason
        super().__init__(reason)


def get_save(eget_save: dict):
    with open(Path('send.html'), 'rb') as fd:
        return fd.read()


def post_save(save_env: dict):
    expected_keys = ('first_name', 'last_name', 'age')
    payload = save_env['wsgi.input'].read(int(save_env['CONTENT_LENGTH']))
    data = parse_qs(payload.decode())
    if len(data) != len(expected_keys):
        raise HTTPError('Bad Request', 400)

    for key in expected_keys:
        if key not in data:
            raise HTTPError('Bad Request', 400)

    return get_save(save_env)


def get_search(env: dict):
    with open(Path('search.html'), 'rb') as fd:
        return fd.read()


def post_search(search_env: dict):
    expected_keys = ('first_name', 'last_name', 'age')
    payload = search_env['wsgi.input'].read(int(search_env['CONTENT_LENGTH']))
    data = parse_qs(payload.decode())
    if len(data) != len(expected_keys):
        raise HTTPError('Bad Request', 400)

    for key in expected_keys:
        if key not in data:
            raise HTTPError('Bad Request', 400)
    with open('data.json', 'a+') as fp:
        json.dump(data, fp)
        fp.write("\n")
    return get_search(search_env)


def get_search_res(env: dict):
    data = parse_qs(env['QUERY_STRING'])
    expected_keys = ['search']
    serach = data['search'][0].split(' ')
    first_name = serach[0]
    last_name = serach[1]
    if len(data) != len(expected_keys):
        raise HTTPError('Bad Request ', 400)
    for key in expected_keys:
        if key not in data:
            raise HTTPError('Bad Request', 400)
    t = False  # ardyoq gtel e hamn@nknum
    with open('data.json', 'r') as fd:
        for line in fd:
            d = json.loads(line)
            if d['first_name'][0] == first_name and d['last_name'][0] == last_name:
                age = d['age'][0]
                t = True
                break
    if not t:
        return "<h1> People data who you search is not exist in file </h1".encode()
    return "<h2>First Name {} </h2><h2>Last name {}</h2><h2>Age {}</h2>".format(first_name, last_name, age).encode()


def not_found(env: dict):
    raise HTTPError('Not Found', 404)


ROUTING_TABLE = {
    '/send': {
        'GET': get_save,
        'POST': post_save,
    },
    '/search': {
        'GET': get_search,
        'POST': post_search,
    },
    '/search/res': {
        'GET': get_search_res,
    }

}


def app(env: dict, start_response: Callable) -> Iterable:
    route = env['PATH_INFO']
    method = env['REQUEST_METHOD']

    try:
        handler = ROUTING_TABLE.get(route, {}).get(method, not_found)
        response = handler(env)

        start_response('200 OK', [('Content-type', 'text/html')])
        return [response]
    except HTTPError as herr:
        start_response(f'{herr.code} {herr.reason}', [('Content-type', 'text/html')])
        return [f'<h2>{herr.code} {herr.reason}</h2>'.encode()]


if __name__ == '__main__':
    with make_server('127.0.1.1', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
