from django.core.management import BaseCommand
import requests
from businesses.models import Restaurant
from businesses.views import ByCityView

API_KEY = "opTdRYx0KXISF4awBOx-1icw6vBNTjLu1ewpH7mQ_md4tS_IOR8iVl11_e4Jd80jBqVoWSGa_jxSJ7UQLTA3ebUWOe0Du8Cbfh7f4Z17yQL0vaHlsWd4oFIqa0YmaHYx"
headers= {"Authorization": f"Bearer {API_KEY}"}
# params = {"term":"restaurants", "location":"Orlando", "limit":50}
params = {"term":"restaurants", "location":city, "limit":50}
url = "https://api.yelp.com/v3/businesses/search"

class Command(BaseCommand):
    def handle(self, *args, **options):
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        for i in data['businesses']:
            place_name = i['name']
            cuisine = i['categories'][0]['title']
            image_url =  i['image_url']
            rating = i['rating']
            try:
                price = len(i['price'])
            except:
                price = 0
            street = i['location']['address1']
            city = i['location']['city']
            state = i['location']['state']
            zip_code = i['location']['zip_code']
            phone = i['display_phone']
            obj, created = Restaurant.objects.get_or_create(
                place_name = place_name,
                cuisine = cuisine,
                image_url = image_url,
                rating = rating,
                price = price,
                street = street,
                city = city,
                state  = state,
                zip_code = zip_code,
                phone = phone
            )
            print(obj,created)
