from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarView, NewCarView


urlpatterns = [
    path('cars/', CarView.as_view(), name='cars_list'),
    path('new_car/', NewCarView.as_view(), name='new_car')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
