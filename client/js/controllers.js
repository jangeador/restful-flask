var clientControllers = angular.module('clientControllers', []);

clientControllers.controller("TaskListCtrl", ['$scope', 'Task', function($scope, Task) {
  Task.query(function(data) {
    $scope.tasks = data;
    console.log;
  });
}]);