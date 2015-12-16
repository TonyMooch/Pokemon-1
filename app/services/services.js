'use strict';

/* Services */

var pokemonServices = angular.module('pokemonServices', ['ngResource']);

pokemonServices.factory('Pokemon', ['$resource',
  function($resource){
    return $resource('test_data/pikachu.json', {}, {
      query: {method:'GET', params:{}}
    });
  }]);
