from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view(name='deform_static', path='deform:static')
    config.add_static_view(name='static', path='mysite:static')
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')
    config.scan()
    return config.make_wsgi_app()
