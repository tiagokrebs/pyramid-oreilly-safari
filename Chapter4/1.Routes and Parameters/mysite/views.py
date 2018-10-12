from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config


@view_config(route_name='list', renderer='templates/list.jinja2')
def list(request):
    return dict()


@view_config(route_name='add', renderer='templates/add.jinja2')
def add(request):
    return dict() # retorna sem parametros


@view_config(route_name='view', renderer='templates/view.jinja2')
def view(request):
    current = request.matchdict.get('id') # obtem chave id do dict
    return dict(current=current) # passa id obtido como parametro de retorno 'current'


@view_config(route_name='edit', renderer='templates/edit.jinja2')
def edit(request):
    current = request.matchdict.get('id')
    return dict(current=current)


@view_config(route_name='delete')
def delete(request):
    url = request.route_url('list') # rota do 'list'
    return HTTPFound(url) # retorna url para redirecionamento
