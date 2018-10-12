from pyramid.config import Configurator
# adicionada importacao sqlalchemy
from pyramid_sqlalchemy import metadata


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    # como o software nao vai funcionar sem sqlalchemy ele deve ser importado aqui tb
    # alem dos arquivos de configuracao
    config.include('pyramid_sqlalchemy')
    config.add_static_view(name='deform_static', path='deform:static')
    config.add_static_view(name='static', path='mysite:static')
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')
    config.scan()
    # create_all nesse ponto permite que as views sejam criadas primeiro
    # depois verifia e cria os modelos do projeto no banco de dados
    metadata.create_all()
    return config.make_wsgi_app()
