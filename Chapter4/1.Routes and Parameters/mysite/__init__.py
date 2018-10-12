from pyramid.config import Configurator

# 5 rotas definidas para o todo app
def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_route('list', '/')
    config.add_route('add', '/add')
    config.add_route('view', '/{id}') #{id} é um parametro da rota
    config.add_route('edit', '/{id}/edit')
    config.add_route('delete', '/{id}/delete')
    config.scan()
    return config.make_wsgi_app()
