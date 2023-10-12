from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView


urlpatterns = [
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
