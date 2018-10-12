from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config


class MySite:
    def __init__(self, request):
        self.request = request

    @property
    def current(self):
        return self.request.matchdict.get('id')

    @notfound_view_config(renderer='templates/notfound.jinja2')
    def not_found(self):
        return dict()

    @view_config(route_name='list', renderer='templates/list.jinja2')
    def list(self):
        return dict()

    @view_config(route_name='add', renderer='templates/add.jinja2')
    def add(self):
        return dict()

    @view_config(route_name='view', renderer='templates/view.jinja2')
    def view(self):
        if self.current != '1':
            raise HTTPNotFound()
        return dict()

    @view_config(route_name='edit', renderer='templates/edit.jinja2')
    def edit(self):
        return dict()

    @view_config(route_name='edit', renderer='templates/edit.jinja2',
                 request_method='POST')
    def edit_handler(self):
        new_title = self.request.params.get('new_title')
        print ('New title', new_title)
        url = self.request.route_url('list')
        return HTTPFound(url)

    @view_config(route_name='delete')
    def delete(self):
        url = self.request.route_url('list')
        return HTTPFound(url)
