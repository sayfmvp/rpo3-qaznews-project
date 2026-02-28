from django.contrib import admin
from django.urls import path, include # include-ты қосуды ұмытпа
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')), # core_app-тағы urls-ты қосамыз
]

# Суреттер (image) дұрыс көрінуі үшін мына жолдар міндетті:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
