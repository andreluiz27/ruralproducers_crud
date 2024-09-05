from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import  RuralProducerCreateView

urlpatterns = [
    path('', RuralProducerCreateView.as_view(), name='ruralproducer-list-create'),

    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
