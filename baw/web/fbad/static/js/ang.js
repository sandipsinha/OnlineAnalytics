 
var app1=angular.module('app1',[]);

app1.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{a');
  $interpolateProvider.endSymbol('a}');
}]);
app1.controller('GetFBAdDataCtrl', function($scope, $http) {
	    $scope.loading=true;
		$http.get("/apiv1/solar/solardb")
	    .then(function(response) {
	    	if (response.data.length > 0) {
	    	$scope.loading=false;	
	        $scope.liveUsers = response.data[0]['no_of_players'];

	    }
	    })
	    
   });


 
	   