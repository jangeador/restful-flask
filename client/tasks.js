var app = angular.module('myApp', ['ngResource']);

app.factory('Task', [$resource, function($resource) {
  return $resource("http://127.0.0.1:5000/tasks");
}]);


app.controller("TaskList", ['$scope', 'Task', function($scope, Task) {
  Task.query(function(data) {
    $scope.tasks = data;
  });
}]);
