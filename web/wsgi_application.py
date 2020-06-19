import os
from typing import Iterable
from urllib.parse import parse_qs

def application(env: dict, start_response: callable) -> Iterable:
    qs = parse_qs(env['QUERY_STRING'])
    html_path = os.path.abspath(os.path.join('html', env['PATH_INFO'].lstrip('/')))
    if os.path.isfile(html_path):
        with open(html_path, 'rb') as fd:
            html = fd.read()

        start_response(
            '200 OK',
            [
                ('Content-type', 'text/html'),
                ('Content-lenght', str(len(html)))
            ]
        )
        return [html]

    start_response('404 Not Found', [])
    return [b'<h1>Nothing found here</h1>']
