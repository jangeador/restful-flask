var clientServices = angular.module('clientServices', ['ngResource']);

clientServices.factory('Task', '$resource', function($resource) {
  return $resource("http://127.0.0.1:5000/tasks");
});
