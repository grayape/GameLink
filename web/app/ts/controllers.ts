/// <reference path='../_all.ts' />

module app {
    'use strict'
    
    export class LogCtrl {
        constructor ($scope){
            $scope.logType = "customer2";
        }
    }

    export class EntryCtrl  extends LogCtrl {
        injection = ['$scope'];

    
        constructor($scope, $http) {
            super($scope)
          
            
            $http.get('logs/' + $scope.logType + '.log').success(function(data) {
                var log = new Log(data)
                $scope.entries = log.getEntries()
            });
            
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
