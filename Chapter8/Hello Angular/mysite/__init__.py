from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view(name='static', path='mysite:static')
    config.add_route('home', '/')
    config.add_route('greeting', '/greeting')
    config.scan()
    return config.make_wsgi_app()
