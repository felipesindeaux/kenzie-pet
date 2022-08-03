from django.urls import path

from animals.views import AnimalsView

from . import views

urlpatterns = [
    path('animals/', views.AnimalsView.as_view()),
    path('animals/<int:id>/', views.AnimalViewById.as_view())
]
