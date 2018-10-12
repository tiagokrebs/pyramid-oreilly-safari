from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

from pyramid_sqlalchemy import metadata


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.scan()
    config.include('pyramid_sqlalchemy')
    metadata.create_all()
    config.add_static_view(name='deform_static', path='deform:static')
    config.add_static_view(name='static', path='mysite:static')
    config.add_route('home', '/')
    config.add_route('todos_list', '/todos')
    config.add_route('todos_add', '/todos/add')
    config.add_route('todos_view', '/todos/{id}')
    config.add_route('todos_edit', '/todos/{id}/edit')
    config.add_route('todos_delete', '/todos/{id}/delete')

    # obtem secret definido em arquido de configuracao
    session_secret = settings['session.secret']
    # instancia a session_factory do pyeamid
    # atencao session_factory do pyramid nao é para producao
    # os dados nao sao criptografados
    # usa-se em desenvolvimento mas nao em producao
    session_factory = SignedCookieSessionFactory(session_secret)
    config.set_session_factory(session_factory)

    return config.make_wsgi_app()
