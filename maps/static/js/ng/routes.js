var app = angular.module("maps", ["ngRoute", "ngSanitize", "mapsControllers", "mapsDirectives", "mapsServices", "LocalStorageModule"]);

app.config(['$routeProvider','$httpProvider', '$locationProvider',
    function($routeProvider, $httpProvider, $locationProvider) {

        $locationProvider
            .html5Mode(false)
            .hashPrefix('!');

        $routeProvider.
            when('/dashboard', {
                templateUrl: 'ng/templates/dashboard',
                controller: 'dashboardCtrl'
            }).
            when('/add-route', {
                templateUrl: 'ng/templates/add-route',
                controller: 'routeAddCtrl'
            }).
            when('/route/:id', {
                templateUrl: 'ng/templates/route',
                controller: 'routeCtrl'
            }).
            when('/login', {
                templateUrl: 'ng/templates/login',
                controller: 'loginCtrl'
            }).
            otherwise({
                redirectTo: '/dashboard'
            });
    }]);

app.run(function($window, $rootScope, $location, $timeout, localStorageService, mapsService) {

    //
    // listen for device online/offline events
    //

    $rootScope.online = navigator.onLine;
    $window.addEventListener("offline", function () {
        $rootScope.$apply(function() {
            $rootScope.online = false;
        });
    }, false);

    $window.addEventListener("online", function () {
        $rootScope.$apply(function() {
            $rootScope.online = true;
        });
    }, false);

    //
    // Caching stuff
    //

    // start off declaring the app 'cached' if the app isn't set to run in cached mode (i.e in "development" mode)
    $rootScope.app_is_cached = $('html').attr('manifest') === undefined;

    // store initial application cache value from local storage
    if (localStorageService.get('app_is_cached') === null) {
        localStorageService.set('app_is_cached', $rootScope.app_is_cached);
    } else {
        // sets the application cache status on the scope
        $rootScope.app_is_cached = localStorageService.get('app_is_cached') === 'true';
    }

    // attribute which indicates total cache failure
    $rootScope.app_cache_error = false;

    var processCacheEvent = function (event) {

        var valid_cache_events = ['noupdate', 'cached', 'updateready'];

        // event indicating the app is cached
        if ($.inArray(event.type, valid_cache_events) != -1) {
            localStorageService.set('app_is_cached', true);
            $rootScope.$apply(function() {
                $rootScope.app_is_cached = true;
                $rootScope.app_cache_error = false;
            });
        }
        // if the app hasn't been successfully cached and we get an error, then it's a critical one
        else if (event.type == 'error' && ! $rootScope.app_is_cached) {
            $rootScope.$apply(function() {
                $rootScope.app_cache_error = true;
            });
        }

        // the cache manifest has changed which means we need to update the cache by reloading
        if (event.type == 'updateready') {
            $window.location.reload();
        }
    };

    $window.applicationCache.addEventListener('checking',processCacheEvent,false);
    $window.applicationCache.addEventListener('noupdate',processCacheEvent,false);
    $window.applicationCache.addEventListener('downloading',processCacheEvent,false);
    $window.applicationCache.addEventListener('progress',processCacheEvent,false);
    $window.applicationCache.addEventListener('cached',processCacheEvent,false);
    $window.applicationCache.addEventListener('updateready',processCacheEvent,false);
    $window.applicationCache.addEventListener('obsolete',processCacheEvent,false);
    $window.applicationCache.addEventListener('error',processCacheEvent,false);

    //
    // authentication stuff
    //

    // set the current username in the root scope
    $rootScope.username = localStorageService.get('username');

    // checks if there's a username in local storage
    $rootScope.logged_in = function () {
        var username = localStorageService.get('username');
        return username && username.length > 0;
    };

    $rootScope.logout = function () {
        mapsService.logout()
            .success(function (result) {

                console.log("successfully logged out");

                localStorageService.remove('username');
                $rootScope.username = '';

                // keep the unsynced routes on logout
                var routes = localStorageService.get('routes') || [];
                var routes_to_keep = [];

                for (var i in routes) {
                    if (! routes[i].synced) {
                        routes_to_keep.push(routes[i]);
                    }
                }

                localStorageService.set('routes', routes_to_keep);

                // redirect back to login page
                $location.path('/login');
            })
            .error(function(result) {
                $rootScope.error = 'An unknown error occurred when trying to log out';
                console.log($rootScope.error);
            });
    };

    // go to login page if it doesn't appear we're logged in
    if (! $rootScope.logged_in()) {
        $location.path('/login');
    }

    //
    // helpers
    //

    //go to path
    $rootScope.go = function (path) {
        $('body').plainOverlay('show');
        $timeout(function () {
            $location.path(path)
        }, 1000);
    };
});
