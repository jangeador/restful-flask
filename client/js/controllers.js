var clientControllers = angular.module('clientControllers', []);

var ws="http://ws.gosanluis.com/tasks"

clientControllers.controller("TaskListCtrl", ['$scope', '$http', function ($scope, $http) {
    $http.get(ws).success(function (data) {
        $scope.tasks = data;
    });
}]);

//var artistControllers = angular.module('artistControllers', []);
//
//artistControllers.controller('ListController', ['$scope', '$http', function ($scope, $http) {
//    $http.get('js/data.json').success(function (data) {
//        $scope.artists = data;
//        $scope.artistOrder = 'name';
//    });
//}]);
//
//artistControllers.controller('DetailsController', ['$scope', '$http', '$routeParams', function ($scope, $http, $routeParams) {
//    $http.get('js/data.json').success(function (data) {
//        $scope.artists = data;
//        $scope.whichItem = $routeParams.itemId;
//    });
//}]);

