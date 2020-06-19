from wsgiref.simple_server import make_server
import configparser
import importlib

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.INI')
    ip = config.get('server', 'ip')
    port = int(config.get('server', 'port'))
    moduel_name = config.get('app', 'module')
    app_name = config.get('app', 'app')
    mymodule = importlib.import_module(moduel_name)
    wsgi_app = getattr(mymodule, app_name)
    '''#TODO: use values from 'wsgi_server.conf' for server configuration
    # TODO: import WSGI callable application dynamically from configuration
    # NOTES: following modules may be helpful
    #        https://docs.python.org/3/library/importlib.html
    #        https://docs.python.org/3/library/configparser.html'''
    with make_server(ip, port, wsgi_app) as httpd:
        print('Serving on port {port}...')
        httpd.serve_forever()
