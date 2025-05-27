from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Restaurant

from .models import Restaurant

def greeting_function(request):
    return render(
    request,
    "businesses/greeting.html",
    context= {"Message": "Hello world!"}
    )


class RestaurantListView(ListView):
    model = Restaurant
    def get_context_data(self, **kwargs):
        context =  super(RestaurantListView, self).get_context_data(**kwargs)
        cities = set([i.city for i in self.object_list])
        print(cities)
        context["all_cities"] = list(cities)
        return context
class RestaurantDetailView(DetailView):
    model = Restaurant

class RestaurantCreateView(CreateView):
    model = Restaurant
    fields = [
        "place_name",
        "cuisine",
        "image_url",
        "rating",
        "price",
        "street",
        "city",
        "state",
        "zip_code",
        "phone"
    ]

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    fields = [
        "place_name",
        "cuisine",
        "image_url",
        "rating",
        "price",
        "street",
        "city",
        "state",
        "zip_code",
        "phone"
    ]

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    success_url = reverse_lazy('list-view')

class ByCityView(ListView):
    model = Restaurant
    template_name = "businesses/restaurant_list.html"

    # def load_sity(self, city):
    #     API_KEY = "opTdRYx0KXISF4awBOx-1icw6vBNTjLu1ewpH7mQ_md4tS_IOR8iVl11_e4Jd80jBqVoWSGa_jxSJ7UQLTA3ebUWOe0Du8Cbfh7f4Z17yQL0vaHlsWd4oFIqa0YmaHYx"
    #     headers = {"Authorization": f"Bearer {API_KEY}"}
    #     # params = {"term":"restaurants", "location":"Orlando", "limit":50}
    #     params = {"term": "restaurants", "location": city, "limit": 50}
    #     url = "https://api.yelp.com/v3/businesses/search"
    #     response = requests.get(url, params=params, headers=headers)
    #     data = response.json()
    #     for i in data['businesses']:
    #         place_name = i['name']
    #         cuisine = i['categories'][0]['title']
    #         image_url =  i['image_url']
    #         rating = i['rating']
    #         try:
    #             price = len(i['price'])
    #         except:
    #             price = 0
    #         street = i['location']['address1']
    #         city = i['location']['city']
    #         state = i['location']['state']
    #         zip_code = i['location']['zip_code']
    #         phone = i['display_phone']
    #         obj, created = Restaurant.objects.get_or_create(
    #             place_name = place_name,
    #             cuisine = cuisine,
    #             image_url = image_url,
    #             rating = rating,
    #             price = price,
    #             street = street,
    #             city = city,
    #             state  = state,
    #             zip_code = zip_code,
    #             phone = phone
    #         )
    #         print(obj,created)

    def get_context_data(self, **kwargs):

        print("hgjhg")
        context =  super(ByCityView, self).get_context_data(**kwargs)
        city_to_find = self.kwargs["city"]
        filtered_restaurants = Restaurant.objects.filter(city__icontains=city_to_find)
        if len(filtered_restaurants)==0:
            self.load_sity(city_to_find)
            filtered_restaurants = Restaurant.objects.filter(city__icontains=city_to_find)
        number_of_rest = len(filtered_restaurants)
        context["rest_found"] = filtered_restaurants
        context["number_of_rest"] = number_of_rest
        context["city"] = city_to_find.capitalize()
        context["message"] = "Art says Hi!"
        print("Thats what we found", context)
        return context
