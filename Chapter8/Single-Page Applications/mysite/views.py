import os

from pyramid.response import FileResponse
from pyramid.view import view_config, view_defaults

sample_todos = [
    dict(id=1, title='Get Milk'),
    dict(id=2, title='Get Eggs')
]


@view_config(route_name='app_html')
def index_view(request):
    here = os.path.dirname(__file__)
    index_path = os.path.join(here, 'app', 'index.html')
    return FileResponse(index_path, request=request)


@view_defaults(renderer='json')
class ToDos:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='todos_list')
    def todos_list(self):
        return sample_todos
