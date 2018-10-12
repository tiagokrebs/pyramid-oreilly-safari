function ToDoFactory($resource) {
    return $resource('/api/todos');
}

function HomeCtrl() {
}

function ToDosCtrl(ToDo) {
    this.todos = ToDo.query();
}

angular.module('app', ['ngResource'])
    .factory('ToDo', ToDoFactory)
    .controller('HomeCtrl', HomeCtrl)
    .controller('ToDosCtrl', ToDosCtrl);