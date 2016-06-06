(function() {
    function CommonAppController($scope, $rootScope, APIServices, $state, $http, $stateParams, $window) {
        $scope.getdata = function() {
            var getData = APIServices.getData();
            getData.success(function(data) {
                $scope.result = data;
            }).error(function(data) {});
        }
        //get
        $scope.getdata();

        $scope.getDataPop = function(name){
        	//console.log($stateParams);
        	//alert('calling'+'________'+name);
        	var url = "http://localhost:8000/monitordetails"+name+"/?proname="+$stateParams.id+"&mtype="+name;

        	$http.get(url).success( function(response) {
        		$('body').append('<div class="modalPop"><div class="modalClose"></div></div>');

		    	 $('.modalPop').append(response);

		    	 $('.modalClose').on('click', function(){
		    	 	$('.modalPop').remove();
		    	 	$window.location.href = 'http://localhost/html/devops/app/#/';
		    	 	$window.location.reload();
		    	 });
		   	});
        }
        

        $scope.getDetails = function(clientName) {
        	// $scope.clientName=clientName;
            $rootScope.nameList = [];
            for (var i = 0; i < $scope.result.length; i++) {
                if (!$scope.result[i].client.localeCompare(clientName)) {
                    $rootScope.nameList.push({
                        name: $scope.result[i].check.name,
                        status: $scope.result[i].check.status
                    });
                }
            }
            $state.go("name",{"id":clientName});

        }

        $scope.styleClient = function(clientName) {
            var color = [];
            for (var i = 0; i < $scope.result.length; i++) {
                if (!$scope.result[i].client.localeCompare(clientName)) {
                    color.push($scope.result[i].check.status);
                    $scope.status = $scope.result[i].check.status
                }
            }

            var result = color.max();

            console.log(result);
            if (result == 0) {
                return "imgGreen";
            } else if (result == 1) {
                return "imgOrange";
            } else if (result == 2) {
                return "imgRed";
            } else {
                return "imgBlue";
            }

        }
        Array.prototype.max = function() {
            return Math.max.apply(Math, this);
        };

        $scope.styleFunction = function(no) {
            if (no == 0) {
                return "imgGreen";
            } else if (no == 1) {
                return "imgOrange";
            } else if (no == 2) {
                return "imgRed";
            } else {
                return "imgBlue";
            }


        }

    }
    var app = angular.module("devops").controller("CommonAppController", CommonAppController);
})();
