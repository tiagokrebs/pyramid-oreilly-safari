import os

from pyramid.response import FileResponse
from pyramid.view import view_config, view_defaults


@view_config(route_name='app_html')
def index_view(request):
    here = os.path.dirname(__file__)
    index_path = os.path.join(here, 'app', 'index.html')
    return FileResponse(index_path, request=request)


@view_defaults(renderer='json')
class ToDos:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(route_name='todos')
    def todos(self):
        return self.context.list()

    @view_config(route_name='todos', request_method='POST')
    def todos_add(self):
        title = self.request.json_body['title']
        todo = self.context.add(title=title)
        return todo

    @view_config(route_name='todo')
    def todo_view(self):
        return self.context

    @view_config(route_name='todo', request_method='PUT')
    def todo_edit(self):
        self.context.title = self.request.json_body['title']
        return self.context

    @view_config(route_name='todo', request_method='DELETE')
    def todo_delete(self):
        self.context.__class__.delete(self.context)
        return dict()
