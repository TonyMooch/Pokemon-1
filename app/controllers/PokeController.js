app.controller('PokeController', ['$scope', function($scope) {
  $scope.pokemon = {
     name: 'Pikachu',
     type: 'Electric'
  };
  $scope.active = true;
}]);