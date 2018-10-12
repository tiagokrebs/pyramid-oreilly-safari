from pyramid.httpexceptions import HTTPFound, HTTPNotFound
from pyramid.view import view_config, notfound_view_config

# nova classe mysite
# essa classe tem varios metodos decorados view_configs
# transformando eles em views com uma rota registrada
# nesse formato pyramid trata a requisição em 2 etapas
# primeiro uma instancia da classe é criada
# depois a rota que meljor atende é atendida
# com a classe instanciada disponivel
# dentro de view.jinja2 é possível usar classe.current
class MySite:
    def __init__(self, request):
        self.request = request

    # essa propriedade permite classe obter um dado da requisição
    # e disponibiliza-lo como um atributo da classe
    # é possóvel usar @view_dafaults para as views da classe para atributos padrão a todas
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
