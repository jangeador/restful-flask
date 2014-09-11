var clientControllers = angular.module('clientControllers', []);

clientControllers.controller("TaskListCtrl", ['$scope', '$http', function ($scope, $http) {
    $http.get('http://127.0.0.1:5000').success(function (data) {
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

