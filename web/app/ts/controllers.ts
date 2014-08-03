/// <reference path='../_all.ts' />

module app {
    'use strict'
    
    export class LogCtrl {
        constructor ($scope){
            $scope.logType = "customer2";
        }
    }
    
    export class PlayersCtrl {
        injection = ['$scope'];

        constructor ($scope,$filter,ngTableParams){
            $scope.players = [
            {name:'Rasmus',id:1,matches_played:1},
            {name:'Kim',id:2,matches_played:1}
            ];

            $scope.tableParams = new ngTableParams({
                    page: 1,            // show first page
                    count: 10,          // count per page
                    sorting: {
                        name: 'asc'     // initial sorting
                    }
                }, {
                    counts: [], // hide page counts control
                    total: 1,  // value less than count hide pagination
                    getData: function($defer, params) {
                        // use build-in angular filter
                        var orderedData = params.sorting() ?
                                            $filter('orderBy')($scope.players, params.orderBy()) :
                                            $scope.players;

                        $defer.resolve(orderedData);
                        //$defer.resolve(orderedData.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                    }
                });
            }
    }

    export class EntryCtrl  extends LogCtrl {
        injection = ['$scope'];

    
        constructor($scope, $http) {
            super($scope)
          
            $scope.entries = [1,2,3];
            //$http.get('logs/' + $scope.logType + '.log').success(function(data) {
            //    var log = new Log(data)
            //    $scope.entries = log.getEntries()
            //});
            
        }
    }

    export class SessionCtrl extends LogCtrl{
        injection = ['$scope'];

    
        constructor($scope , $http) {
           super($scope)
            $http.get('logs/' + $scope.logType + '.log').success(function(data) {
                var log = new Log(data)
                $scope.sessions = log.getSessions();
                
            });

            
        }
    }

}
