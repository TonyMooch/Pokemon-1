'use strict';

angular.module('PokeApp.pokeInfo', ['ngRoute', 'pokemonServices'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/pokeResult', {
    templateUrl: 'views/pokeInfo.html',
    controller: 'PokeResultController'
  });
}])
.controller('PokeResultController', ['$scope', 'Pokemon', function($scope, Pokemon) {
	$scope.info = Pokemon.query();
}]);