var services = angular.module("mapsServices", []);

services.factory('mapsService', ["$http", "localStorageService", "$location", "$rootScope",
    function($http, localStorageService, $rootScope) {

        var section_completed = function (route, index, name) {
            return percent_complete(route, index, name);
        };

        var percent_complete_all = function (route) {

            if (! route.sections || ! route.sections.length) {
                return 0;
            }

            var total = 0;
            angular.forEach(route.sections, function (section, index) {
                total += percent_complete(route, index, section.name);
            });

            return Math.floor((total/route.sections.length));
        };

        var percent_complete = function (route, index, name) {

            // flag 100% complete for "shared" sections.  They don't need to be completed again
            if ($.inArray(name, Array('segment', 'crossing', 'culdesac')) != -1) {
                if (route.sections[index]['form']['id']) {
                    return 100;
                }
            }

            var surveys = localStorageService.get('surveys') || [];
            var survey = surveys[route.survey_id];

            var number_items = function (items) {
                var total = 0;
                for (var i in items) {
                    if (items[i].subitems.length) {
                        total += number_items(items[i].subitems);
                    } else {
                        total += 1;
                    }
                }
                return total;
            };

            // tally up unique item ids
            var number_unique_item_entries = function (entries) {
                var unique_item_entries = [];
                for (var i in entries) {
                    var exists = false;
                    for (var k in unique_item_entries) {
                        if (entries[i].item_id == unique_item_entries[k].item_id && entries[i].is_sub_item == unique_item_entries[k].is_sub_item) {
                            exists = true;
                        }
                    }
                    // make sure it's got an actual value
                    if (! exists && entries[i].value != null) {
                        unique_item_entries.push(entries[i]);
                    }
                }
                return unique_item_entries.length;
            };

            var completed_form_fields = function (fields, required_fields) {

                var completed = 0;

                angular.forEach(fields, function (field, name) {
                    if ($.inArray(name, required_fields) != -1 && field) {
                        completed++;
                    }
                });

                return completed;
            };

            var entries = number_unique_item_entries(route.sections[index].entries);
            var items = number_items(survey[name+'_items']);

            // tally up required form fields
            var required_form_fields_for_section = survey[route.sections[index].name+'_required_form_fields'];
            if (required_form_fields_for_section) {
                entries += completed_form_fields(route.sections[index].form, required_form_fields_for_section);
                items += required_form_fields_for_section.length;
            }

            return Math.floor((entries/items) * 100);
        };

        // save a route
        var update_route = function (route, skip_sync) {

            // explicitly flag that this route was just synced so no need to set it as false
            if (! skip_sync) {
                route.synced = false;
            }

            // set the end time if this route is now completed
            if (percent_complete_all(route) == 100) {
                route.end_time = Math.ceil(new Date().getTime() / 1000);
            }

            var routes = localStorageService.get('routes') || [];
            for (var i in routes) {
                if (route.id == routes[i].id) {
                    routes[i] = route;
                }
            }
            localStorageService.set('routes', routes);
        };

        // save gps coordinates
        var save_coords = function (route, section_index) {
            if(navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(
                    // success
                    function(position) {

                        console.log('Latitude: %s', position.coords.latitude);
                        console.log('Longitude: %s', position.coords.longitude);

                        // lookup this route in storage, add the coords, then save routes back
                        var routes = localStorageService.get('routes');
                        for (var i in routes) {
                            if (routes[i].id == route.id) {
                                routes[i].sections[section_index].coords = position.coords;
                                localStorageService.set('routes', routes);
                                return;
                            }
                        }
                    },
                    // error
                    function() {
                        console.log('GPS position error');
                    }
                );
            } else {
                console.log('Geo Location not available');
            }
        };

        return {

            percent_complete_all: percent_complete_all,
            percent_complete: percent_complete,
            section_completed: section_completed,
            update_route: update_route,
            save_coords: save_coords,

            // upper case first word
            uc_first: function(word) {
                return word.charAt(0).toUpperCase() + word.slice(1);
            },

            // login
            login: function (username, password) {
                return $http.post('ng/templates/login?post', {username: username, password: password});
            },

            // logout
            logout: function () {
                return $http.post('ng/templates/logout');
            },

            // sync an individual route
            sync_route: function (route) {
                return $http.post('entries/submit', route);
            },

            // pull down all the incomplete entries/items for this user
            download_incomplete_routes: function (scope) {

                var promise = $http.get('entries/retrieve');

                promise.then(function (result) {

                    // session expired
                    if(result.data.hasOwnProperty('errorCode') && result.data.errorCode == 'not-logged-in') {
                        scope.error = result.data.errorMessage;
                        scope.needs_login = true;
                        localStorageService.remove('username');
                        $rootScope.username = null;
                        $('body').plainOverlay('hide');
                        return;
                    }

                    var existing_routes_ids = [];

                    var existing_routes = localStorageService.get('routes') || [];
                    var surveys = localStorageService.get('surveys') || [];

                    // gather all existing routes on the device to copmare against
                    angular.forEach(existing_routes, function (route, index) {
                        existing_routes_ids.push(route.id);
                    });

                    // add in downloaded routes that don't exist on device
                    angular.forEach(result.data, function (route, index) {

                        // make sure each item has an id for safe error handling
                        if (!route.hasOwnProperty('id')) {
                            return;
                        }

                        // add if it's not already in the existing routes
                        if ($.inArray(route.id, existing_routes_ids) == -1) {
                            existing_routes.push(route);
                            console.log('saving route', route);
                        }
                    });
                    localStorageService.set('routes', existing_routes);
                });

                return promise;
            },

            // get all the surveys and their items
            surveys: function (scope) {

                console.log('Loading surveys from server');

                var promise = $http.get('surveys/items');

                promise.then(function(result) {

                    var i;
                    var surveys = [];

                    // check that each result has an id for safe error handling
                    for (i in result.data) {
                        if (!result.data[i].hasOwnProperty('id')) {
                            continue;
                        }
                        surveys.push(result.data[i]);
                    }

                    // no surveys returned so lets load from local storage
                    if (! surveys.length) {
                        scope.surveys = localStorageService.get('surveys');
                    } else {
                        scope.surveys = {};
                        for (i in surveys) {
                            scope.surveys[surveys[i].id] = surveys[i];
                        }
                    }

                    console.log('loaded these surveys', scope.surveys);

                    localStorageService.set('surveys', scope.surveys);
                });

                return promise;
            },

            // indicates whether a route id exists or not in local storage
            route_exists: function (id, routes) {
                for (var i in routes) {
                    if (id == routes[i].id) {
                        return true;
                    }
                }
                return false;
            },

            not_applicable_value: '-777',

            // save/update an item entry into local storage
            update_entry: function(ctrl_route, section, section_index, entry) {

                // returns the location of an existing entry, if any
                var entry_position = function (entry, entries, match_value) {

                    for (var i in entries) {

                        var e = entries[i];

                        // matching items
                        if (e.item_id == entry.item_id && e.is_sub_item == entry.is_sub_item) {

                            // testing to see if the entry's value matches as well
                            if (match_value) {
                                if (e.value == entry.value) {
                                    return i;
                                }
                            } else {
                                return i;
                            }
                        }
                    }
                    // didn't find an existing entry
                    return -1;
                };

                // get the routes from storage
                var routes = localStorageService.get('routes');

                angular.forEach(routes, function (route) {

                    if (route.id == ctrl_route.id) {

                        // set gps coords on this section if it's the first entry
                        if (! route.sections[section_index].entries.length) {
                            save_coords(ctrl_route, section_index);
                        }

                        route.synced = false;

                        // set the start time if it doesn't exist yet
                        if (! ctrl_route.hasOwnProperty('start_time')) {
                            ctrl_route.start_time = Math.ceil(new Date().getTime() / 1000);
                            route.start_time = ctrl_route.start_time;
                        }

                        var position;

                        //////////////////////////////////////////////////////////
                        // depending on the item type, we may need to
                        //  - add/remove the entry (select-multiple, i.e. a checkbox)
                        //  - update the entry (select, text, number)
                        //////////////////////////////////////////////////////////

                        if (entry.item_type == 'select') {
                            // position of the entry if it exists
                            position = entry_position(entry, route.sections[section_index].entries, false);
                            if (position != -1) {
                                route.sections[section_index].entries.splice(position, 1);
                            }
                            route.sections[section_index].entries.push(entry);
                        }
                        else if (entry.item_type == 'select-multiple') {
                            // position of the entry if it exists and match the value itself too
                            position = entry_position(entry, route.sections[section_index].entries, true);
                            // option exists already, so remove it
                            if (position != -1) {
                                route.sections[section_index].entries.splice(position, 1);
                            }
                            // otherwise add it
                            else {
                                route.sections[section_index].entries.push(entry);
                            }
                        } else if (entry.item_type == 'text' || entry.item_type == 'number') {
                            // position of the entry if it exists
                            position = entry_position(entry, route.sections[section_index].entries, false);
                            if (position != -1) {
                                route.sections[section_index].entries.splice(position, 1);
                            }
                            route.sections[section_index].entries.push(entry);
                        }

                        // update the scope's route's entries as well
                        ctrl_route.sections = route.sections;

                        // set the end time if this route is now completed
                        if (percent_complete_all(ctrl_route) == 100) {
                            ctrl_route.end_time = Math.ceil(new Date().getTime() / 1000);
                            route.end_time = ctrl_route.end_time;
                        }

                        // we done updated
                        return;
                    }
                });

                // persist the change to storage
                localStorageService.set('routes', routes);
            }
        }
}]);
