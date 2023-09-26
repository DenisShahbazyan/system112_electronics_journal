from urllib.parse import urlencode

from django.core.paginator import Paginator

from journal.settings import COUNT_POST_FOR_PAGE

from .filters import PostFilter
from .search import search_posts


def include_paginator(request, db_object):
    """Пагинатор для постов.

    Args:
        request (django.core.handlers.wsgi.WSGIRequest): объект запроса.
        db_object (QuerySet): список объектов из базы данных.

    Returns:
        Paginator: пагинатор
    """
    paginator = Paginator(db_object, COUNT_POST_FOR_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def get_GET_params_for_paginator(request, params: tuple[str]):
    """Вспомогательная функция для сохранения параметров GET запроса, 
    используется для пагинатора, чтоб при перелистывании страниц, запрос 
    сохранялся.

    К примеру, если запрос такой:
        <QueryDict: {'tags': ['instrukcii', 'paroli'], 'q': ['qwe']}>
    то функция вернет такую строку:
        &tags=instrukcii&tags=paroli&q=qwe

    Args:
        request (request): запрос Django.
        params (tuple): кортеж запросов из которых нужно составить url.

    Returns:
        str: строка запроса.
    """
    query_dict = request.GET

    query_items = []
    for key, val_list in query_dict.lists():
        if key not in params:
            continue
        for val in val_list:
            query_items.append((key, val))

    query_string = urlencode(query_items, doseq=True)
    return '&' + query_string if query_string else query_string


def search_and_filter(request, queryset):
    """Функция поиска и фильтрации постов.

    Args:
        request (request): запрос Django.
        queryset (QuerySet): список объектов из базы данных.

    Returns:
        QuerySet: список объектов из базы данных.
    """
    posts = PostFilter(request.GET, queryset=queryset).qs
    posts = search_posts(request, posts)
    return posts
