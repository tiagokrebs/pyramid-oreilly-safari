# imports
# wsgi padrão pyramid
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

# view ou wsgi app
# passa um parametro pyramid request vazio
# retorna objeto simples de resposta pyramid, o texto que se ve no browser
def hello(request):
    return Response('Hello world!')

# sessão de execução de módulos
# usa medoto padrão python para modulos que rodam sozinhos
# o código dentro desse if roda apenas se for executado pelo comando python no sheel
if __name__ == '__main__':
    config = Configurator() # cria a instancia do pyramid configurator
    config.add_route('hello_world', '/') # adicona rota para mapear uma url até uma view
    config.add_view(hello, route_name='hello_world') # define via configurator um nome para a rota
    app = config.make_wsgi_app() # a partir daqui levanta o serviço wsgi para aguardar requests
    server = make_server('0.0.0.0', 6543, app)
    print ('Serving at http://127.0.0.1:6543')
    server.serve_forever()
