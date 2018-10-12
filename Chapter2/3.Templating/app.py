# para renderizar html diretamente de uma funcao
# usam-se templates para gerar html a partir de dados
# usa jinja2
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.view import view_config

# adiciona uma nova configuração a view o arquivo renderizado
# graças a isso a view precisa retornar apenas um dicionario de dados
# em vez da resposta html
@view_config(route_name='hello_world', renderer='hello.jinja2')
def hello(request):
    return dict(name='World') # pyramid pega esse retorno da view passa por dentro do template jinja2 e retorna o resultado do template


if __name__ == '__main__':
    config = Configurator()
    config.include('pyramid_jinja2') # inclue comandos do pacote pyramid_jinja2 (renderizador)
    # Isso vincula todos os arquivos com extensao .jinja2 serem renderizados pelo pacote
    config.add_route('hello_world', '/')
    config.scan()
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    print ('Serving at http://127.0.0.1:6543')
    server.serve_forever()
