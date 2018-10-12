import os, random

from pyramid.response import FileResponse
from pyramid.view import view_config, view_defaults

sample_todos = [
    dict(id=1, title='Get Milk'),
    dict(id=2, title='Get Eggs')
]


def todo_factory(request):
    todo_id = int(request.matchdict.get('id'))
    for todo in sample_todos:
        if todo['id'] == todo_id:
            return todo


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
        return sample_todos

    @view_config(route_name='todos', request_method='POST')
    def todos_add(self):
        new_id = random.randint(1111, 9999)
        new_title = self.request.json_body['title']
        sample_todos.append(dict(id=new_id, title=new_title))
        return dict(id=new_id, title=new_title)

    @view_config(route_name='todo')
    def todo_view(self):
        return self.context

    @view_config(route_name='todo', request_method='PUT')
    def todo_edit(self):
        self.context['title'] = self.request.json_body['title']
        return self.context

    @view_config(route_name='todo', request_method='DELETE')
    def todo_delete(self):
        sample_todos.remove(self.context)
        return dict()
