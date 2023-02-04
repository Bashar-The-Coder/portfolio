from django.urls import path, include
from . import views

app_name = "port"

urlpatterns = [
    path("" , views.index , name= 'index'),
    path("about/" , views.about , name= 'about'),
    path("resume/" , views.resume , name= 'resume'),
    path("portfolio/" , views.portfolio , name= 'portfolio'),
    path("services/" , views.services , name= 'services'),
    path("contact/" , views.contact , name= 'contact'),
]
