from datetime import datetime


def year(request):
    """Создание перемнной с текущим годом. Используется для footer'а."""
    return {'year': datetime.now().year}
