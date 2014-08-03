/// <reference path='../_all.ts' />

module app {
    'use strict'

    var myapp: ng.IModule = angular.module('zebralogApp', ['ngRoute','ngTable'])

    myapp.controller('SessionCtrl', SessionCtrl)
    myapp.controller('EntryCtrl', EntryCtrl)
    // myapp.service('service', ScaffoldService.prototype.injection())

    // myapp.directive('directive', ScaffoldDirective.prototype.injection())

    myapp.config(['$routeProvider', function($routeProvider: ng.route.IRouteProvider) {
    $routeProvider.
    when('/entries', {templateUrl: 'partials/entries.html', controller: EntryCtrl}).
    when('/sessions', {templateUrl: 'partials/sessions.html', controller: SessionCtrl}).
    when('/players', {templateUrl: 'partials/players.html', controller: PlayersCtrl}).
    
    otherwise({redirectTo: '/logs'})
    }])
}



// 'use strict';

// /* App Module */

// var zebralogApp = angular.module('zebralogApp', [
//   'ngRoute',
//   'zebralogControllers'
// ]);

// zebralogApp.config(['$routeProvider',
//   function($routeProvider) {
//     $routeProvider.
//       when('/logs', {
//         templateUrl: 'partials/logs.html',
//         controller: 'LogCtrl'
//       }).
//       when('/phones/:phoneId', {
//         templateUrl: 'partials/phone-detail.html',
//         controller: 'PhoneDetailCtrl'
//       }).
//       otherwise({
//         redirectTo: '/logs'
//       });
//   }]);
