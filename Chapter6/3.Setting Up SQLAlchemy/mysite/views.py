from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config

import colander
from deform import Form, ValidationFailure


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
        self.msg = request.params.get('msg')

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
        return dict(todos=sample_todos.values())

    @view_config(route_name='todos_add',
                 renderer='templates/add.jinja2')
    def add(self):
        return dict(add_form=self.form.render())

    @view_config(route_name='todos_add',
                 renderer='templates/add.jinja2',
                 request_method='POST')
    def add_handler(self):
        controls = self.request.POST.items()
        try:
            appstruct = self.form.validate(controls)
        except ValidationFailure as e:
            # Form is NOT valid
            return dict(add_form=e.render())

        # Valid so (fake) add a new ToDoItem to the database,
        # then redirect
        title = appstruct['title']
        msg = 'new_title: ' + title
        url = self.request.route_url('todos_list', _query=dict(msg=msg))
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
        controls = self.request.POST.items()
        try:
            appstruct = self.form.validate(controls)
        except ValidationFailure as e:
            # Form is NOT valid
            return dict(edit_form=e.render())

        # Valid form so save the title and redirect with message
        self.current['title'] = appstruct['title']
        msg = 'new_title: ' + appstruct['title']
        url = self.request.route_url('todos_view',
                                     id=self.current['id'],
                                     _query=dict(msg=msg))
        return HTTPFound(url)

    @view_config(route_name='todos_delete')
    def delete(self):
        msg = 'Deleted: ' + self.current['id']
        url = self.request.route_url('todos_list', _query=dict(msg=msg))
        return HTTPFound(url)

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()
