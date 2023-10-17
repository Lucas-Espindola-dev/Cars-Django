from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView


class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        # Nesse query, todos os modelos são retornados da mesma forma que retorna no objects.all().
        # O super faz referência a ListView. A utilização de super() é para invocar a herança.
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search).order_by('model')
        return cars


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'
    # Pagina seguinte.


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarUpdate(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'
