from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .settings import DEBUG, MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('about/', include('about.urls', namespace='about')),
    path("ckeditor5/", include('django_ckeditor_5.urls'),
         name="ck_editor_5_upload_file"),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)


handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'
