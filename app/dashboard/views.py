from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .forms import RuralProducerForm, RuralProducerUpdateForm
from rural_producer.models import RuralProducer
from django.shortcuts import redirect, render
from crop.models import Crop
from farm.models import Farm


class RuralProducerCreateView(CreateView):
    template_name = "dashboard.html"
    success_url = "/analytics/"

    def get_form(self, form_class=None):
        return RuralProducerForm()

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        ruralproducer_form = RuralProducerForm(request.POST)
        if ruralproducer_form.is_valid():
            ruralproducer_form.save()
        else:
            print(ruralproducer_form.errors)
            return render(request, "dashboard.html", {"form": ruralproducer_form})
        return redirect("/analytics/")


class RuralProducerUpdateView(UpdateView):
    template_name = "rural_producer_edit.html"
    success_url = "/analytics/"

    def get_queryset(self):
        return RuralProducer.objects.all()

    def get_form(self, form_class=None):
        return RuralProducerUpdateForm()

    def get_context_data(self, **kwargs):
        # gettint initials 
        context = super().get_context_data(**kwargs)
        context["form"] = RuralProducerUpdateForm(
            initial={
                "name": self.object.name,
                "cpf_cnpj": self.object.cpf_cnpj,
                "city": self.object.farm.city,
                "state": self.object.farm.state,
                "farm_name": self.object.farm.farm_name,
                "farm_area": self.object.farm.farm_area,
                "vegetation_area": self.object.farm.vegetation_area,
                "plantable_area": self.object.farm.plantable_area,
                "crops": self.object.farm.crops.all(),
            }
        )
        return context    

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        ruralproducer_form = RuralProducerUpdateForm(request.POST)
        if ruralproducer_form.is_valid():
            ruralproducer_form.save(pk=kwargs.get("pk"))
        else:
            print(ruralproducer_form.errors)
            return render(request, "rural_producer_edit.html", {"form": ruralproducer_form})
        return redirect("/analytics/")
          
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import DeleteView

class RuralProducerDeleteView(DeleteView):
    model = RuralProducer
    success_url = reverse_lazy('analytics')  # Using reverse_lazy to ensure URL resolution

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        rural_producer = self.get_object()  # Get the RuralProducer instance
        farm_id = rural_producer.farm.id
        rural_producer.delete()  # Delete the RuralProducer instance
        Farm.objects.get(id=farm_id).delete()  # Delete the associated Farm instance
        return redirect(self.success_url)


class RuralProducerListView(ListView):
    model = RuralProducer
    template_name = "rural_producer_list.html"
    context_object_name = "rural_producer"

    def get_queryset(self):
        return RuralProducer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rural_producers"] = RuralProducer.objects.all()
        return context


class AnalyticsView(ListView):
    model = RuralProducer
    template_name = "analytics.html"
    context_object_name = "rural_producer"

    def get_queryset(self):
        return RuralProducer.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rural_producers"] = RuralProducer.objects.all()

        all_farms = Farm.objects.all()
        context["total_farms"] = all_farms.count()
        context["total_crops"] = Crop.objects.all().count()
        context["total_area"] = sum([farm.farm_area for farm in all_farms])
        context["total_vegetation_area"] = sum(
            [farm.vegetation_area for farm in all_farms]
        )
        context["total_plantable_area"] = sum(
            [farm.plantable_area for farm in all_farms]
        )

        all_rural_producers = RuralProducer.objects.all()
        context["total_rural_producers"] = all_rural_producers.count()

        # total crops of all farms
        context["total_crops"] = sum([farm.crops.count() for farm in all_farms])

        def adding_to_crops_dict(crop_plantation, crops_dicts):
            if crop_plantation in crops_dicts:
                crops_dicts[crop_plantation] += 1
            else:
                crops_dicts[crop_plantation] = 1
            return crops_dicts

        crops_in_farm = {}
        for farm in all_farms:
            for crop in farm.crops.all():
                crop_plant = Crop.objects.get(id=crop.id)
                adding_to_crops_dict(crop_plant.crop_plantation, crops_in_farm)

        context["crops_in_farm"] = crops_in_farm

        # getting states analytics
        states = {}
        for farm in all_farms:
            if farm.state in states:
                states[farm.state] += 1
            else:
                states[farm.state] = 1

        context["states"] = states
        return context
