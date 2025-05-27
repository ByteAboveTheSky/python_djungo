from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Car
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class CarListView(ListView):
    model = Car
    def get_context_data(self, **kwargs):
        context = super(CarListView, self).get_context_data(**kwargs)
        colors = set([i.color for i in self.object_list])
        context["all_colors"] = list(colors)
        return context

class CarDetailView(DetailView):
    model = Car

class CarCreateView(CreateView):
    model = Car
    fields = '__all__'

class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'blog/car_form.html'

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("list-view")

class ByColorView(ListView):
    model = Car
    template_name = 'old_car_list.html'

    def get_context_data(self, **kwargs):
        context = super(ByColorView, self).get_context_data(**kwargs)
        # print("______________ context:",context)
        # print("______________ context_car:",context['object_list'])

        filtered_cars = Car.objects.filter(color = self.kwargs["color"])
        context["filtered_cars"] = filtered_cars
        context["color"] = self.kwargs["color"]
        context["filter_type"] = "color"
        print(filtered_cars)
        return context

class ByMakeView(ListView):
    model = Car
    template_name = 'old_car_list.html'
    def get_context_data(self, **kwargs):
        context = super(ByMakeView, self).get_context_data(**kwargs)
        filtered_cars = Car.objects.filter(make=self.kwargs["make"])
        context["filtered_cars"] = filtered_cars
        context["make"] = self.kwargs["make"]
        context["filter_type"] = "make"
        print(filtered_cars)
        return context