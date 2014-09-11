var clientControllers = angular.module('clientControllers', []);

var ws="http://ws.gosanluis.com/tasks"

clientControllers.controller("TaskListCtrl", ['$scope', '$http', function ($scope, $http) {
    $http.get(ws).success(function (data) {
        $scope.tasks = data;
        //$scope.msg = "Ehlo"

        function done(task, taskState){
            task.done = taskState;
            $scope.msg = 'clicked ' + task.title;
        };

        $scope.done = done;

    });
}]);

