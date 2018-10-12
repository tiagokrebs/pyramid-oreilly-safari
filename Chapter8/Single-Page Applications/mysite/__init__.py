from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.add_route('todos_list', '/api/todos')
    config.scan()

    # Statically serve app directory at the "/" URL
    config.add_static_view(name='/', path='mysite:app')
    config.add_route('app_html', '/')

    return config.make_wsgi_app()
