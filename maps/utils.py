from maps.models import SUB_ITEM


def build_item(item):
    """
    :type item: maps.models.Item
    """

    # build options
    options = []
    for option in item.itemoption_set.all():
        options.append({'id': option.id, 'title': option.title, 'value': option.value})

    # build sub-items
    subitems = []
    if item.type == SUB_ITEM:
        for subitem in item.subitem_set.all():
            subitems.append(build_item(subitem))

    helper = None
    helpers = item.itemhelper_set.all()
    if helpers.exists():
        helper = helpers[0].content

    return {
        'id': item.id,
        'title': item.title,
        'type': item.type,
        'options': options,
        'include_not_applicable': item.include_not_applicable,
        'subitems': subitems,
        'helper': helper,
    }
