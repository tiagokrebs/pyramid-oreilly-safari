from pyramid.view import view_config

class MySite:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='home', renderer='templates/home.jinja2')
    def home(self):
        return dict()

    @view_config(route_name='greeting', renderer='json')
    def greeting(self):
        greeting = 'Hello %s!' % self.request.json_body.get('name')
        return dict(greeting=greeting)
