from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    # chama area do projeto com arquivos estaticos para serem chamados pelo browser
    # static = arquivos que nao vao ser interpretados ou executados pelo pyramid
    # forma de pyramid servir arquivos que estçao no servidor sem necessidade de código
    config.add_static_view(name='static', path='mysite:static') # ':' define asssts specifications.
    # é possível linkar arquivos diferentes de outros pacotes dessa forma
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')
    config.scan()
    return config.make_wsgi_app()
