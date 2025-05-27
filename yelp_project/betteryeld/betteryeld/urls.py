"""
URL configuration for betteryeld project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from businesses.views import greeting_function
from businesses.views import (
                            RestaurantListView,
                            RestaurantDetailView,
                            RestaurantCreateView,
                            RestaurantUpdateView,
                            RestaurantDeleteView,
                            ByCityView,
                        )

urlpatterns = [
    path("admin/", admin.site.urls),
    path('greeting/', greeting_function),
    path("", RestaurantListView.as_view(), name='list-view'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='detail-view'),
    path('restaurant/create/', RestaurantCreateView.as_view(), name='create-view'),
    path('restaurant/update/<int:pk>', RestaurantUpdateView.as_view(), name='update-view'),
    path('restaurant/delete/<int:pk>', RestaurantDeleteView.as_view(), name='delete-view'),
    path("restaurant/search/<city>/", ByCityView.as_view(), name="search_city")
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

