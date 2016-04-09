var ctrls = angular.module("mapsControllers", []);

ctrls.controller("loginCtrl", ["$rootScope", "$scope", "localStorageService", "$location", "$route", "$window", "mapsService",
    function($rootScope, $scope, localStorageService, $location, $route, $window, mapsService) {

        //
        // functions
        //

        $scope.clear_error = function () {
            $scope.error = false;
        };

        $scope.login = function () {
            mapsService.login($scope.username, $scope.password)
                .success(function (result) {
                    if (result.success) {
                        console.log("successfully logged in with %s", result.username);
                        localStorageService.set('username', result.username);

                        // now try and retrieve surveys from server if there's none in local storage
                        mapsService.surveys($scope)
                            .success(function () {
                                // redirect to base URL
                                $window.location.href=document.URL.substring(0, document.URL.indexOf('#'));
                            })
                            .error(function () {
                                $scope.error = 'An error occurred when trying to retrieve surveys after sign-in. Could not connect.';
                            });
                    } else {
                        $scope.error = 'Username and/or password is incorrect';
                        console.log($scope.error);
                    }
                })
                .error(function(result) {
                    $scope.error = 'An error occurred when trying to sign in. Could not connect.';
                    console.log($scope.error);
                });
        };

        // go to dashboard if we're already logged in
        if ($rootScope.logged_in()) {
            $location.path('/');
        }

        $scope.error = false;

        $('body').plainOverlay('hide');
    }]);

ctrls.controller("dashboardCtrl", ["$rootScope", "$scope", "localStorageService", "$location", "$timeout", "mapsService",
    function($rootScope, $scope, localStorageService, $location, $timeout, mapsService) {

        //
        // functions
        //

        $scope.download_incomplete_routes = function() {

            // clear any existing errors
            $scope.clear_error();

            $('body').plainOverlay('show');

            mapsService.download_incomplete_routes($scope)
                .success(function () {
                    $('body').plainOverlay('hide');
                    $scope.init();
                })
                .error(function() {
                    $scope.error = 'There was an error when trying to download routes. Unable to connect.';
                    $('body').plainOverlay('hide');
                });
        };

        $scope.get_error = function () {
            return $rootScope.error || $scope.error;

        };

        $scope.clear_error = function () {
            $rootScope.error = false;
            $scope.error = false;
            $scope.needs_login = false;
        };

        $scope.remove_synced_and_completed = function () {

            // clear any errors if they exist
            $scope.clear_error();

            var confirmed = confirm(
                'Are you sure you want to remove all synced and completed routes?\n\nALL DATA ON DEVICE WILL BE LOST!');

            // copy the scope's routes into a local variable since the delete_route function updates the scope's value
            var routes = $scope.routes.slice();

            if (confirmed) {
                for (var i in routes) {
                    if (routes[i].synced && mapsService.percent_complete_all(routes[i]) == 100) {
                        $scope.delete_route(routes[i].id, true);
                    }
                }
            }

            // populate route rows again
            $scope.init();
        };

        $scope.sync_all = function () {

            // clear any errors if they exist
            $scope.clear_error();

            for (var i in $scope.routes) {
                // only sync dirty routes
                if (! $scope.routes[i].synced) {
                    $scope.sync_route($scope.routes[i]);
                }
            }
        };

        $scope.sync_route = function (route) {

            $('body').plainOverlay('show');

            // clear any errors if they exist
            $scope.clear_error();

            $timeout(function () {

                // flag if this route is complete before syncing to server
                route.completed = $scope.route_completed(route);

                mapsService.sync_route(route)
                    .success(function (result) {
                        if (result.success) {
                            route.synced = true;
                            mapsService.update_route(route, true);
                            console.log('Successfully sunk', result);
                        } else if(result.errorCode == 'not-logged-in') {
                            console.log('Not successful sync', result);
                            $scope.error = result.errorMessage;
                            $scope.needs_login = true;
                            localStorageService.remove('username');
                            $rootScope.username = null;
                        } else {
                            $scope.error = 'There was an unknown error during sync.';
                            console.log($scope.error, result);
                        }
                        $('body').plainOverlay('hide');
                    })
                    .error(function(result) {
                        $scope.error = 'There was an error during sync. Could not connect';
                        console.log($scope.error, result);
                        $('body').plainOverlay('hide');
                    });

                }, 1000);
        };

        $scope.route_completed = function (route) {
            return mapsService.percent_complete_all(route) == 100;
        };

        $scope.percent_complete_all = mapsService.percent_complete_all;

        $scope.delete_route = function(id, skip_confirmation) {

            // clear any errors if they exist
            $scope.clear_error();

            var confirmed = false;

            if (skip_confirmation) {
                confirmed = true;
            } else {
                confirmed = confirm("Are you sure you want to delete route#" + id + "?\n\nALL DATA ON DEVICE WILL BE LOST!");
            }

            if (confirmed) {

                // delete from routes
                for (var i in $scope.routes) {
                    if ($scope.routes[i].id == id) {
                        $scope.routes.splice(i, 1);
                        break;
                    }
                }

                // delete from the route rows too
                for (var i in $scope.route_rows) {
                    // iterate over all the row's columns
                    for (var k in $scope.route_rows[i]) {
                        if ($scope.route_rows[i][k].id == id) {
                            $scope.route_rows[i].splice(k, 1);
                            break;
                        }
                    }
                }

                localStorageService.set('routes', $scope.routes);
            }
        };

        $scope.num_routes = function () {
            return $scope.routes.length;
        };

        $scope.num_complete = function () {
            var num_complete = 0;
            for(var i in $scope.routes) {
                if (mapsService.percent_complete_all($scope.routes[i]) == 100) {
                    num_complete++;
                }
            }
            return num_complete;
        };

        $scope.num_incomplete = function () {
            return $scope.num_routes() - $scope.num_complete();
        };

        $scope.num_synced = function () {
            var num_synced = 0;
            for(var i in $scope.routes) {
                if ($scope.routes[i].synced) {
                    num_synced++;
                }
            }
            return num_synced;
        };

        $scope.need_sync = function () {
            return $scope.num_routes() != $scope.num_synced();
        };

        $scope.has_synced_and_completed = function () {
            var num_synced_and_completed = 0;
            for(var i in $scope.routes) {
                if ($scope.routes[i].synced && mapsService.percent_complete_all($scope.routes[i]) == 100) {
                    num_synced_and_completed++;
                }
            }
            return num_synced_and_completed > 0;
        };

        //
        // init
        //

        $scope.init = function () {

            // go to login page if it doesn't appear we're logged in
            if (! $rootScope.logged_in()) {
                $location.path('/login');
            }

            $scope.surveys = localStorageService.get('surveys') || [];

            // get browser's geolocation permission
            if(navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function() {});
            }

            $scope.error = false;

            $scope.routes = localStorageService.get('routes') || [];

            // populate survey name for each route
            angular.forEach($scope.routes, function (route) {
                for (var i in $scope.surveys) {
                    if (route.survey_id == $scope.surveys[i].id) {
                        route.survey_title = $scope.surveys[i].title;
                    }
                }
            });

            $scope.route_rows = [];

            // populate route_rows with two routes per row
            var row_index = 0;
            for (var i=0; i < Math.ceil($scope.routes.length/2); i++) {
                var row = $scope.routes.slice(row_index, row_index + 2);
                $scope.route_rows.push(row);
                row_index += 2;
            }

            $('body').plainOverlay('hide');
        };

        $scope.init();
    }]);


ctrls.controller("routeAddCtrl", ["$rootScope", "$scope", "$routeParams", "$http", "$location", "mapsService", "localStorageService",
    function($rootScope, $scope, $routeParams, $http, $location, mapsService, localStorageService) {

        //
        // functions
        //

        $scope.clear_error = function () {
            $rootScope.error = false;
            $scope.error = false;
        };

        $scope.get_error = function () {
            return $rootScope.error || $scope.error;

        };

        // we only want this controller to be able to change the route's survey type
        // this is just a flag to the template to enable this field
        $scope.can_change_survey = true;

        $scope.route_exists = function(id) {
            return mapsService.route_exists(id, $scope.routes);
        };

        // add a new route and either start it immediately or return to dashboard
        $scope.create_route = function(begin) {

            var survey = $scope.surveys[$scope.route.survey_id];

            $scope.route.synced = false;
            $scope.route.username = $rootScope.username;

            // start off with the route section if there's route items included in the survey
            if (survey.route_items.length) {
                $scope.route.sections = [{
                    name: 'route',
                    entries: []
                }];
            } else {
                // otherwise start off empty
                $scope.route.sections = [];
            }

            // default segment and crossing sections

            var segment = {
                'name': 'segment',
                'entries': [],
                form: {},
                required_form_fields: survey['segment_required_form_fields']
            };

            var crossing = {
                'name': 'crossing',
                'entries': [],
                form: {},
                required_form_fields: survey['crossing_required_form_fields']
            };

            // the "mini segment" survey type has the following sections, in order: crossing, section, crossing
            if (survey.survey_type == 'mini_segment') {
                $scope.route.sections.push(crossing);
                $scope.route.sections.push(segment);
                $scope.route.sections.push(crossing);
            } else {
                // otherwise every route needs to start off with one segment
                $scope.route.sections.push(segment);
            }

            // add the route to our list of routes
            $scope.routes.push($scope.route);

            // save routes back to storage
            localStorageService.set('routes', $scope.routes);

            console.log('creating route', $scope.route);

            // change view to edit route
            if (begin) {
                $location.path('/route/' + $scope.route.id);
            } else { // send them back to the dashboard
                $location.path('/dashboard');
            }
        };

        //
        // MAIN
        //

        $scope.routes = localStorageService.get('routes') || [];
        $scope.route = {};

        $scope.surveys = localStorageService.get('surveys') || [];

        $('body').plainOverlay('hide');
    }]);

ctrls.controller("routeCtrl", ["$rootScope", "$scope", "$routeParams", "$http", "$location", "$route", "$timeout", "mapsService", "localStorageService",
    function($rootScope, $scope, $routeParams, $http, $location, $route, $timeout, mapsService, localStorageService) {

        //
        // functions
        //

        $scope.clear_error = function () {
            $rootScope.error = false;
            $scope.error = false;
        };

        $scope.get_error = function () {
            return $rootScope.error || $scope.error;

        };

        $scope.section_completed = mapsService.section_completed;
        $scope.percent_complete_all = mapsService.percent_complete_all;
        $scope.percent_complete = mapsService.percent_complete;

        $scope.can_delete_section = function () {

            // survey type "mini segment" cannot add/remove sections
            if ($scope.survey.survey_type == 'mini_segment') {
                return false;
            }

            return true;
        };
        $scope.can_add_section = function (section) {

            // survey type "mini segment" cannot add/remove sections
            if ($scope.survey.survey_type == 'mini_segment') {
                return false;
            }

            // make sure we even have items for this section
            if ($scope.survey.hasOwnProperty(section + '_items')) {
                if ($scope.survey[section + '_items'].length) {
                    return true;
                }
            }

            return false;
        };

        $scope.populate_route = function () {

            var routes = localStorageService.get('routes') || [];

            // populate the route's items from the right survey
            for (var i in routes) {

                if (routes[i].id == $routeParams.id) {

                    // copy the located route and set on this controller
                    $scope.route = angular.copy(routes[i]);

                    // populate the right survey
                    $scope.survey = $scope.surveys[$scope.route.survey_id];
                }
            }
        };

        // populate panel items
        $scope.populate_panels = function () {

            $('body').plainOverlay('show');

            $scope.panels = [];

            var section_counts = {};

            angular.forEach($scope.route.sections, function(section) {

                // keep tallies of the number of each section to include in their titles
                if (! section_counts.hasOwnProperty(section.name)) {
                    section_counts[section.name] = 1;
                } else {
                    section_counts[section.name]++;
                }

                // upper case the section name
                var title = mapsService.uc_first(section.name);

                $scope.panels.push({
                    id: section.name + section_counts[section.name],
                    title: section.name == 'route' ? title : title + ' ' + section_counts[section.name],
                    items: $scope.survey[section.name + '_items'],
                    entries: section.entries,
                    survey_section: section.name,
                    locked: section.name == 'route', // section "route" cannot be deleted
                    // every section except for the main "route" has additional forms so we'll pull in their form urls
                    header_form_url: section.name == 'route' ? false : 'static/templates/'+ section.name +'_form.html'
                });
            });

            $('body').plainOverlay('hide');
        };

        $scope.num_sections = function (name) {

            // calculate the number of segments in the sections
            var num_sections = 0;
            for (var i in $scope.route.sections) {
                if ($scope.route.sections[i].name == name) {
                    num_sections++;
                }
            }

            return num_sections;
        };

        $scope.delete_panel = function (index, name) {

            var confirmed = confirm("Are you sure you want to delete this " + name +"?\n\nALL DATA ON DEVICE WILL BE LOST!");

            if (confirmed) {

                $('body').plainOverlay('show');

                // spin for a couple seconds
                $timeout(function () {

                    // remove the panel
                    $scope.panels.splice(index, 1);

                    // now remove the section and save to storage
                    $scope.route.sections.splice(index, 1);

                    $scope.update_route();

                    $scope.populate_panels();
                }, 1000);
            }
        };

        // add a section to this route
        $scope.add_panel = function (name) {

            $('body').plainOverlay('show');

            $timeout(function () {

                $scope.route.sections.push({
                    name: name,
                    entries: [],
                    form: {},
                    required_form_fields: $scope.survey[name+'_required_form_fields'] || []
                });

                // save the route to local storage
                $scope.update_route();

                // add to the panels
                $scope.panels.push({
                    id: name + $scope.num_sections(name),
                    title: mapsService.uc_first(name) + ' ' + $scope.num_sections(name),
                    items: $scope.survey[name+'_items'],
                    survey_section: name,
                    locked: false,
                    header_form_url: 'static/templates/'+name+'_form.html'
                });

                $('body').plainOverlay('hide');

            }, 1000);
        };

        $scope.route_exists = function (id) {

            // we don't want to incorrectly flag a duplicate for the route we're editing
            if (id == $routeParams.id) {
                return false;
            }
            return mapsService.route_exists(id, $scope.routes);
        };

        // save the scope's route
        $scope.update_route = function (synced) {

            mapsService.update_route($scope.route, synced);
        };

        // save the route info
        $scope.update_route_info = function () {

            if ($scope.route_exists($scope.route.id)) {
                return false;
            }

            // indicate this route is no longer in sync with server
            $scope.route.synced = false;

            // the route id itself was updated so replace the old with the new
            if ($routeParams.id != $scope.route.id) {

                var deleted_old_route = false;
                for (var i in $scope.routes) {

                    // delete the route identified by the old id
                    if ($routeParams.id == $scope.routes[i].id) {
                        $scope.routes.splice(i, 1);
                        deleted_old_route = true;
                        break;
                    }
                }

                // only add this new route if it was truly a new route id
                if (deleted_old_route) {
                    // now add in the new route
                    $scope.routes.push($scope.route);
                }

            } else {
                // other details of the route were updated so search for the route and update it
                for (i in $scope.routes) {
                    if ($scope.route.id == $scope.routes[i].id) {
                        $scope.routes[i] = $scope.route;
                        break;
                    }
                }
            }

            // save the routes back to storage
            localStorageService.set('routes', $scope.routes);

            // the route id didn't change so we have to force a reload
            if ($routeParams.id == $scope.route.id) {
                $route.reload();
                return;
            }

            // otherwise change path to new route id
            $location.path('/route/' + $scope.route.id);
        };

        //
        // MAIN
        //

        $scope.route = {};
        $scope.route.sections = [];

        $scope.routes = localStorageService.get('routes') || [];

        // we don't want the survey type to be changed once route has been created.
        // this is just a flag to the template to disable this field on this controller as the default is true
        $scope.can_change_survey = false;

        // redirect to dashboard if this route id doesn't exist
        if (! mapsService.route_exists($routeParams.id, $scope.routes)) {
            $location.path('/dashboard');
        }

        // populate surveys and items from storage
        $scope.surveys = localStorageService.get('surveys') || [];
        $scope.populate_route();
        $scope.populate_panels();
    }]);
