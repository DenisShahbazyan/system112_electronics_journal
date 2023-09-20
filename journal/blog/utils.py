from django.core.paginator import Paginator

from journal.settings import COUNT_POST_FOR_PAGE


def include_paginator(request, db_object):
    paginator = Paginator(db_object, COUNT_POST_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
