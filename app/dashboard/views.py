from django.views.generic.edit import CreateView
from .forms import RuralProducerForm
from rural_producer.models import RuralProducer


class RuralProducerCreateView(CreateView):
    model = RuralProducer
    form_class = RuralProducerForm
    template_name = 'dashboard.html'
    # fields = ['name', 'cpf', 'city', 'state', 'farm_name', 'farm_area', 'vegetation_area', 'crops']

    def form_valid(self, form):
        return super().form_valid(form)
    
     