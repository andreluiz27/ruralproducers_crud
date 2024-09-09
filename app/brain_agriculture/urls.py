from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from dashboard.views import  RuralProducerCreateView, RuralProducerListView, AnalyticsView, RuralProducerDeleteView, RuralProducerUpdateView

urlpatterns = [
    path('', RuralProducerCreateView.as_view(), name='ruralproducer-create'),
    path('ruralproducer/', RuralProducerListView.as_view(), name='ruralproducer-list'),    
    path('analytics/', AnalyticsView.as_view(), name='analytics'),

    # edit rural producer
    path('ruralproducer/<int:pk>/edit/', RuralProducerUpdateView.as_view(), name='ruralproducer-edit'),    

    # delete rural producer
    path('ruralproducer/<int:pk>/delete/', RuralProducerDeleteView.as_view(), name='ruralproducer-delete'),

    path("admin/", admin.site.urls),
    
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # adding static
    urlpatterns += staticfiles_urlpatterns()