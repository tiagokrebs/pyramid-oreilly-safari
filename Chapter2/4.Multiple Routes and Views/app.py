#imports
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# view da rota home_page passando dicionario com site_name utilizado por home.jinja2
@view_config(route_name='home_page', renderer='home.jinja2')
def home(request):
    return dict(site_name='MyApp')

# view da rota hello para requisições sem o parametro name
@view_config(route_name='hello', renderer='hello_world.jinja2')
def hello_world(request):
    return dict()

# view da rota hello escolhida caso o parametro name seja enviado. pyramid escolhe essa rota por ser a mais semlhante
@view_config(route_name='hello', renderer='hello_name.jinja2',
             request_param='name') #request_param é o metodo para obter parametros de uma url
def hello_name(request):
    name = request.params.get('name')
    return dict(name=name)


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2')
    config.add_route('home_page', '/')
    config.add_route('hello', '/hello')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print('Serving at http://127.0.0.1:6543')
    server.serve_forever()
