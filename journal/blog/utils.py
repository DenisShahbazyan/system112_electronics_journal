from django.core.paginator import Paginator
from django.db.models import Q

from journal.settings import COUNT_POST_FOR_PAGE


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


def search_posts(request, queryset):
    """Поиск для постов.

    Args:
        search_query (str): строка для поиска.

    Returns:
        QuerySet: список объектов из базы данных.
    """
    search_query = request.GET.get('q', '')

    if not search_query:
        return queryset

    search_terms = search_query.split()
    q_objects = Q()
    for term in search_terms:
        q_objects |= (
            Q(text__icontains=term) |
            Q(author__first_name__icontains=term) |
            Q(author__last_name__icontains=term) |
            Q(author__patronymic__icontains=term) |
            Q(author__username__icontains=term)
        )
    return queryset.filter(q_objects)
