from entries.models import *

ITEM_OPTION = 0
SUB_ITEM_OPTION = 1
ITEM_AUXILIARY = 2
SUB_ITEM_AUXILIARY = 3
ITEM_NA = 4
SUB_ITEM_NA = 5

SECTION_CLASSES = {
    'route': (
        EntryRouteItemOption, EntryRouteSubItemOption,
        EntryRouteItemAuxiliary, EntryRouteSubItemAuxiliary,
        EntryRouteItemNA, EntryRouteSubItemNA),

    'segment': (
        EntrySegmentItemOption, EntrySegmentSubItemOption,
        EntrySegmentItemAuxiliary, EntrySegmentSubItemAuxiliary,
        EntrySegmentItemNA, EntrySegmentSubItemNA),

    'crossing': (
        EntryCrossingItemOption, EntryCrossingSubItemOption,
        EntryCrossingItemAuxiliary, EntryCrossingSubItemAuxiliary,
        EntryCrossingItemNA, EntryCrossingSubItemNA),

    'culdesac': (
        EntryCuldesacItemOption, EntryCuldesacSubItemOption,
        EntryCuldesacItemAuxiliary, EntryCuldesacSubItemAuxiliary,
        EntryCuldesacItemNA, EntryCuldesacSubItemNA),
}
