from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config

import colander
from deform import Form

# schema do colander utilizado para formularios (deform)
class ToDoItem(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())


sample_todos = {
    '1': dict(id='1', title='Get Milk'),
    '2': dict(id='2', title='Get Eggs')
}

class MySite:
    def __init__(self, request):
        self.request = request
        self.schema = ToDoItem()
        self.form = Form(self.schema, buttons=('submit',))

    @property
    def current(self):
        todo_id = self.request.matchdict.get('id')
        todo = sample_todos.get(todo_id)
        if not todo:
            raise HTTPNotFound()
        return todo

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        return dict()

    @view_config(route_name='todos_list',
                 renderer='templates/list.jinja2')
    def list(self):
        msg = self.request.params.get('msg')
        return dict(
            todos=sample_todos.values(),
            msg=msg
        )

    @view_config(route_name='todos_add',
                 renderer='templates/add.jinja2')
    def add(self):
        return dict(add_form=self.form.render())

    @view_config(route_name='todos_add',
                 renderer='templates/add.jinja2',
                 request_method='POST')
    def add_handler(self):
        new_title = self.request.params.get('title')
        # We will actually do the add in later sections
        msg = 'new_title: ' + new_title
        url = self.request.route_url('todos_list', _query={'msg': msg})
        return HTTPFound(url)

    @view_config(route_name='todos_view',
                 renderer='templates/view.jinja2')
    def view(self):
        return dict(todo=self.current)

    @view_config(route_name='todos_edit',
                 renderer='templates/edit.jinja2')
    def edit(self):
        edit_form = self.form.render(self.current)
        return dict(todo=self.current, edit_form=edit_form)

    @view_config(route_name='todos_edit',
                 renderer='templates/edit.jinja2',
                 request_method='POST')
    def edit_handler(self):
        new_title = self.request.params.get('title')
        self.current['title'] = new_title
        msg = 'new_title: ' + new_title
        url = self.request.route_url('todos_list', _query={'msg': msg})
        return HTTPFound(url)

    @view_config(route_name='todos_delete')
    def delete(self):
        url = self.request.route_url('todos_list')
        return HTTPFound(url)

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()

