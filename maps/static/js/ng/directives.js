var dirs = angular.module("mapsDirectives", []);

dirs.directive("itemHelperModal", ["$compile", function($compile){
    return {
        restrict: 'A',
        scope: {
            item:"=",
            unique:"="
        },
        templateUrl: "static/templates/modal.html",
        link: function(scope, element, attrs) {
            scope.title = scope.item.title;
            scope.content = scope.item.helper;
            scope.footer = '';
            $compile(element.contents())(scope);
        }
    }
}]);

dirs.directive("itemSubItems", ["$compile", function($compile){
    return {
        restrict: 'A',
        scope: {
            item:"=",
            unique:"=",
            surveysection:"=",
            route:"=",
            entries:"=",
            sectionindex:"@"
        },
        link: function(scope, element, attrs) {
            element.html('<strong>{{ item.title }}</strong><br /><hr />');
            element.append('<div base-item item="item" is-sub-item="1" ng-repeat="item in item.subitems" surveysection="surveysection" route="route" entries="entries" sectionindex="{{ sectionindex }}" />');
            $compile(element.contents())(scope);
        }
    }
}]);

dirs.directive("itemSelectMultiple", ["$compile", "mapsService",
    function($compile, mapsService) {
        return {
            restrict: 'A',
            scope: {
                item:"=",
                unique:"=",
                surveysection:"=",
                route:"=",
                isSubItem:"@",
                entries:"=",
                sectionindex:"@"
            },
            templateUrl: "static/templates/select_multiple.html",
            link: function(scope, element, attrs) {

                // include n/a, but make sure it doesn't already exist
                if (scope.item.include_not_applicable) {
                    var add_na = true;
                    for (var i in scope.item.options) {
                        if (scope.item.options[i].id == '-777') {
                            add_na = false;
                            break;
                        }
                    }
                    if (add_na) {
                        scope.item.options.push({id: "-777", title: "N/A"})
                    }
                }

                // list of checked item options
                scope.checked_options = [];

                // populate this item's selections from the entries
                for (var i in scope.entries) {
                    var entry = scope.entries[i];
                    for (var k in scope.item.options) {
                        // found an entry for this item
                        if (entry.value == scope.item.options[k].id && entry.is_sub_item == scope.isSubItem && entry.item_id == scope.item.id && entry.survey_section == scope.surveysection) {
                            scope.checked_options.push(entry.value);
                        }
                    }
                }

                // indicates whether this option is checked
                scope.is_checked = function (id) {
                    return $.inArray(id, scope.checked_options) != -1;
                };

                // saves the change when an item is checked/unchecked
                scope.changed = function (id) {

                    // "none of the above" so remove all existing options
                    if (id == '-777' && scope.item_position('-777') == -1) {
                        for (var i in scope.checked_options) {
                            mapsService.update_entry(scope.route, scope.surveysection, scope.sectionindex, {
                                item_id: scope.item.id,
                                item_type: 'select-multiple',
                                route_id: scope.route.id,
                                survey_section: scope.surveysection,
                                value: scope.checked_options[i],
                                is_sub_item: scope.isSubItem
                            });
                        }
                        scope.checked_options = [];
                    }
                    // regular option chosen but "none of the above" was already chosen, so remove it first
                    else if (id != '-777' && scope.item_position('-777') != -1) {
                        // remove the "none of the above"
                        scope.checked_options.splice(scope.item_position('-777'), 1);
                        mapsService.update_entry(scope.route, scope.surveysection, scope.sectionindex, {
                            item_id: scope.item.id,
                            item_type: 'select-multiple',
                            route_id: scope.route.id,
                            survey_section: scope.surveysection,
                            value: '-777',
                            is_sub_item: scope.isSubItem
                        });
                    }

                    // try and locate the selected option so we can add / remove it from our checked options
                    var position = scope.item_position(id);
                    if (position == -1) {
                        scope.checked_options.push(id);
                    } else {
                        scope.checked_options.splice(position, 1);
                    }

                    // build the entry for the changed item
                    var entry = {};
                    entry.item_id = scope.item.id;
                    entry.item_type = 'select-multiple';
                    entry.route_id = scope.route.id;
                    entry.survey_section = scope.surveysection;
                    entry.value = id;
                    entry.is_sub_item = scope.isSubItem;

                    // now, finally save it
                    mapsService.update_entry(scope.route, scope.surveysection, scope.sectionindex, entry);
                };

                // indicates whether a particular option is already checked
                scope.item_position = function (id) {
                    return $.inArray(id, scope.checked_options);
                };

                // indicates whether this item has had anything checked at all
                scope.has_checked_items = function () {
                    return scope.checked_options.length > 0;
                };

                $compile(element.contents())(scope);
            }
        }
}]);

dirs.directive("itemSelect", ["$compile", "mapsService",
    function($compile, mapsService) {
        return {
            restrict: 'A',
            scope: {
                item:"=",
                unique:"=",
                surveysection:"=",
                route:"=",
                isSubItem:"@",
                entries:"=",
                sectionindex:"@"
            },
            templateUrl: "static/templates/select.html",
            link: function(scope, element, attrs) {

                // include n/a, but make sure it doesn't already exist
                if (scope.item.include_not_applicable) {
                    var add_na = true;
                    for (var i in scope.item.options) {
                        if (scope.item.options[i].id == '-777') {
                            add_na = false;
                            break;
                        }
                    }
                    if (add_na) {
                        scope.item.options.push({id: "-777", title: "N/A"})
                    }
                }

                // indicates whether this item has had anything checked at all
                scope.has_selected = function () {
                    return scope.option_selected;
                };

                scope.is_selected = function (id) {
                    // look for this item's entry
                    for (var i in scope.entries) {
                        var entry = scope.entries[i];
                        // found an entry for this item
                        if (entry.value == id && entry.is_sub_item == scope.isSubItem && entry.item_id == scope.item.id && entry.survey_section == scope.surveysection) {

                            // flag that we selected an item
                            scope.option_selected = true;

                            return true;
                        }
                    }
                    return false;
                };

                // saves the change when an item is checked
                scope.changed = function (id) {

                    // flag that we selected an item
                    scope.option_selected = true;

                    // build the entry for the changed item
                    var entry = {};
                    entry.item_id = scope.item.id;
                    entry.item_type = 'select';
                    entry.route_id = scope.route.id;
                    entry.survey_section = scope.surveysection;
                    entry.value = id;
                    entry.is_sub_item = scope.isSubItem;

                    mapsService.update_entry(scope.route, scope.surveysection, scope.sectionindex, entry);
                };
                $compile(element.contents())(scope);
            }
        }
}]);

dirs.directive("itemInput", ["$compile", "mapsService", function($compile, mapsService) {
    return {
        restrict: 'A',
        scope: {
            item:"=",
            unique:"=",
            surveysection:"=",
            route:"=",
            isSubItem:"@",
            entries:"=",
            sectionindex:"@"
        },
        templateUrl: "static/templates/input.html",
        link: function(scope, element, attrs) {

            scope.item = angular.copy(scope.item);

            // pre-populate the input's value if it already exists
            for (var i in scope.entries) {
                var entry = scope.entries[i];
                if (entry.is_sub_item == scope.isSubItem && entry.item_id == scope.item.id && entry.survey_section == scope.surveysection) {

                    // cast the value to an integer for the html5 input type 'number' to work appropriately
                    if (scope.item.type == 'number') {
                        scope.item.value = parseInt(entry.value);
                    } else {
                        scope.item.value = entry.value;
                    }

                    if (entry.value == mapsService.not_applicable_value) {
                        scope.item.checked_not_applicable = true;
                    }
                }
            }

            // save item entry to storage
            var update_entry = function () {

                // build the entry for the changed item
                var entry = {};
                entry.item_id = scope.item.id;
                entry.item_type = scope.item.type;
                entry.route_id = scope.route.id;
                entry.survey_section = scope.surveysection;
                entry.value = scope.item.value;
                entry.is_sub_item = scope.isSubItem;

                // save
                mapsService.update_entry(scope.route, scope.surveysection, scope.sectionindex, entry);
            };

            scope.changed = function () {

                update_entry();

                // a real value was chosen so uncheck the N/A checkbox if it's checked
                if (scope.item.value != mapsService.not_applicable_value && scope.item.checked_not_applicable) {
                    scope.item.checked_not_applicable = false;
                }
            };

            // set an "N/A" value for text inputs if the item is not applicable
            scope.$watch('item.checked_not_applicable', function(newValue, oldValue) {
                if (newValue != oldValue) {
                    if (newValue) {
                        if (scope.item.type == 'text') {
                            scope.item.value = mapsService.not_applicable_value;
                        }
                    } else {
                        scope.item.value = null;
                    }
                    // now update the item entry
                    update_entry();
                }
            });

            $compile(element.contents())(scope);
        }
    }
}]);

dirs.directive("baseItem", ["$compile", function($compile){
    return {
        restrict: 'A',
        scope: {
            item:"=",
            surveysection:"=",
            route:"=",
            isSubItem:"@",
            entries:"=",
            sectionindex:"@"
        },
        link: function(scope, element, attrs) {

            // generate a random string to guarantee unique ids across items
            scope.unique = scope.item.id + (((1+Math.random())*0x10000)|0).toString(16);

            var inner;
            switch (scope.item.type) {
                case 'text':
                case 'number':
                    inner = '<div item-input item="item" unique="unique" surveysection="surveysection" route="route" is-sub-item="{{ isSubItem }}" entries="entries" sectionindex="{{ sectionindex }}" />';
                    break;
                case 'select':
                    inner = '<div item-select item="item" unique="unique" surveysection="surveysection" route="route" is-sub-item="{{ isSubItem }}" entries="entries" sectionindex="{{ sectionindex }}" />';
                    break;
                case 'select-multiple':
                    inner = '<div item-select-multiple item="item" unique="unique" surveysection="surveysection" route="route" is-sub-item="{{ isSubItem }}" entries="entries" sectionindex="{{ sectionindex }}" />';
                    break;
                case 'sub-items':
                    inner = '<div item-sub-items item="item" unique="unique" surveysection="surveysection" route="route" entries="entries" sectionindex="{{ sectionindex }}" />';
                    break;
                default: inner = '<span class="alert alert-danger">Undefined item type directive</span>';
            }
            element.html(inner);
            $compile(element.contents())(scope);
        }
    }
}]);

dirs.directive("surveyRow", ["$compile", function($compile){
    return {
        restrict: 'A',
        scope: {
            items:"=",
            surveysection:"=",
            route:"=",
            entries:"=",
            sectionindex:"@"
        },
        templateUrl: "static/templates/survey_row.html",
        link: function(scope, element, attrs) {
            $compile(element.contents())(scope);
        }
    }
}]);

dirs.directive("survey", ["$compile",
    function($compile){
        return {
            restrict: 'A',
            scope: {
                surveyitems:"=",
                surveysection:"@",
                route:"=",
                entries:"=",
                sectionindex:"="
            },
            template: '<div survey-row ng-repeat="row in rows" items="row" surveysection="surveysection" route="route" entries="entries" sectionindex="{{ sectionindex }}" />',
            link: function(scope, element, attrs) {

                scope.$watch('surveyitems', function(newValue, oldValue) {

                    // items have finished loading
                    if(newValue) {

                        scope.rows = [];
                        var num_cols = 3;
                        var row_index = 0;
                        for (var i = 0; i < scope.surveyitems.length; i++) {
                            var row = scope.surveyitems.slice(row_index, num_cols + row_index);
                            scope.rows.push(row);
                            // no more items
                            if (row.length != 3) {
                                break;
                            }
                            row_index += 3;
                        }
                        $compile(element.contents())(scope);
                    }
                });
            }
        }
    }]);
