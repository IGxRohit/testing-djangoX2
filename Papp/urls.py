from django.urls import path
from Papp import views

urlpatterns = [
  path("",views.home),
  path("about/",views.about)
]