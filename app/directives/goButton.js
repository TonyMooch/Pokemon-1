app.directive('goButton', function() {
  return {
    restrict: 'E',
    scope: {},
    templateUrl: 'directives/goButton.html',
    link: function(scope, element, attrs) {
      scope.buttonText = "go!";
    }
  };
});