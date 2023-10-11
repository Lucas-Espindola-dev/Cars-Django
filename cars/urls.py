from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import new_car_view, CarView


urlpatterns = [
    path('cars/', CarView.as_view(), name='cars_list'),
    path('new_car/', new_car_view, name='new_car')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
