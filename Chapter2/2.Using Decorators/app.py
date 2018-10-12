from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
# importação de im view config decorator
from pyramid.view import view_config

# decoramos a função configurando ela como uma view
# o decorador é muito próximo de uma view function
@view_config(route_name='hello_world')
def hello(request):
    return Response('Hello world!')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('hello_world', '/')
    config.scan() # dizemos ao configurator para procurar e executar qualquer view encontrada nesse pacote
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print ('Serving at http://127.0.0.1:6543')
    server.serve_forever()
