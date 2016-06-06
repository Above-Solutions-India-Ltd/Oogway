angular.module('devops').factory('APIServices', function($http) {
    //call SAILJS RESTful API using post/get
    var API = {};

    API.getData = function() {
        return $http({
            method: 'get',
            url: "http://52.9.185.212:4567/results"
        });
    };

    return API;
});
