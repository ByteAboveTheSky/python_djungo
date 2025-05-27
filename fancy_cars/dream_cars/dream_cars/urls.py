"""
URL configuration for dream_cars project.

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
from garage.views import (CarListView,
                          CarDetailView,
                          CarCreateView,
                          CarUpdateView,
                          CarDeleteView,
                          ByColorView,
                          ByMakeView,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CarListView.as_view(), name="list-view"),
    path("car/create/", CarCreateView.as_view(),name="create-view"),
    path("car/update/<int:pk>/", CarUpdateView.as_view(),name="update-view"),
    path("car/delete/<int:pk>/", CarDeleteView.as_view(),name="delete-view"),
    path("car/<int:pk>/",CarDetailView.as_view(), name='DetailView'),
    path("car/search/color/<color>/",ByColorView.as_view(), name='filter-color-view'),
    path("car/search/make/<make>/",ByMakeView.as_view(), name='filter-make-view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
