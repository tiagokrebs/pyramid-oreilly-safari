function ToDoFactory($resource) {
    return $resource('/api/todos');
}

function HomeCtrl() {
}

function ToDosCtrl(ToDo) {
    this.todos = ToDo.query();
}

function ModuleConfig($routeProvider) {

    $routeProvider.
        when('/', {
            templateUrl: 'home.html',
            controller: 'HomeCtrl as ctrl'
        }).
        when('/todos', {
            templateUrl: 'todos_list.html',
            controller: 'ToDosCtrl as ctrl'
        }).
        otherwise({
            redirectTo: '/'
        });
}

angular.module('app', ['ngResource', 'ngRoute'])
    .factory('ToDo', ToDoFactory)
    .controller('HomeCtrl', HomeCtrl)
    .controller('ToDosCtrl', ToDosCtrl)
    .config(ModuleConfig);