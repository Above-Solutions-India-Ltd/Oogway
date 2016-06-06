'use strict';

var app = angular
    .module('devops', ['ui.router'])
    .config(function($stateProvider, $urlRouterProvider) {
        $urlRouterProvider.otherwise("/");
        $stateProvider
            .state('home', {
                url: "/",
                templateUrl: "partial/home.html",
                controller: "CommonAppController"
            })
            .state('name', {
                url: "/name/:id",
                templateUrl: "partial/name.html",
                controller: "CommonAppController"
            })
            .state('content', {
                url: "/content",
                templateUrl: "partial/content.html",
                controller: "CommonAppController"
            });
    });

app.filter('unique', function() {
   return function(collection, keyname) {
      var output = [], 
          keys = [];

      angular.forEach(collection, function(item) {
          var key = item[keyname];
          if(keys.indexOf(key) === -1) {
              keys.push(key);
              output.push(item);
          }
      });

      return output;
   };
});