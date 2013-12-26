angular.module('weatherApp.controllers', []);

weatherApp.controller('WeatherCtrl', function ($scope, $http) {
    var lat, lng;

    $scope.getPlace = function(){
        url = geocode_root + '?address=' + $scope.place + "&sensor=false";

        $http.get(url).success(function(data) {
            // console.log(data);
            if (data.status === "OK") {
                $scope.results = data.results;
            }
        });
    };

    $scope.getWeather = function(result){
        // console.log(result);
        if (result.hasOwnProperty("geometry") &&
            result.geometry.hasOwnProperty("location")) {
            
            lat = result.geometry.location.lat;
            lng = result.geometry.location.lng;

            $http.get("/api/forecast/" + lat + "/" + lng).success(function(data) {
                console.log(data);
                if (data.hasOwnProperty("currently")) {
                    $scope.weather = {
                        location: result.formatted_address,
                        apparentTemperature: data.currently.apparentTemperature,
                        summary: data.currently.summary,
                        temperature: data.currently.temperature
                    };

                    jQuery('#forecast').slideDown();
                }
            });
        }
    };
});