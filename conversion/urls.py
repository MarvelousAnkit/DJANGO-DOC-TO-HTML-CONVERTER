from django.urls import path
from .views import save_and_convert
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', save_and_convert, name='convert_to_html'),    # other URL patterns for your application
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)