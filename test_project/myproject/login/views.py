from django.shortcuts import render
def login(request):
    return render(request, "login/login.html", context={"name": "Elena"})
# Create your views here.
