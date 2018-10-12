from pyramid.view import view_config

# adicionado path templates
@view_config(route_name='list',
             renderer='templates/list.jinja2')
def list(request):
    return dict()
