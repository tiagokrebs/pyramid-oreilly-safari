from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config

# isso é uma especie de lista com um dicionario de dados
# é usado apenas para ilustrar o problema
# o mais comum é que essas informações estejam no banco de dados
sample_todos = {
    '1': dict(id='1', title='Get Milk'),
    '2': dict(id='2', title='Get Eggs')
}


class MySite:
    def __init__(self, request):
        self.request = request

    @property
    def current(self):
        todo_id = self.request.matchdict.get('id')
        todo = sample_todos.get(todo_id)
        if not todo:
            raise HTTPNotFound()
        return todo

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()

    @view_config(route_name='list', renderer='templates/list.jinja2')
    def list(self):
        msg = self.request.params.get('msg')
        return dict(
            todos=sample_todos.values(),
            msg=msg
        )

    @view_config(route_name='add', renderer='templates/add.jinja2')
    def add(self):
        return dict()

    @view_config(route_name='view', renderer='templates/view.jinja2')
    def view(self):
        return dict(todo=self.current)

    @view_config(route_name='edit', renderer='templates/edit.jinja2')
    def edit(self):
        return dict(todo=self.current)

    @view_config(route_name='edit', renderer='templates/edit.jinja2',
                 request_method='POST')
    def edit_handler(self):
        new_title = self.request.params.get('new_title')
        self.current['title'] = new_title
        msg = 'new_title: ' + new_title
        url = self.request.route_url('list', _query={'msg': msg})
        return HTTPFound(url)

    @view_config(route_name='delete')
    def delete(self):
        url = self.request.route_url('list')
        return HTTPFound(url)
