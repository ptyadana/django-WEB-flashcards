from django.urls import path
from flashcard_app import views

urlpatterns = [
   path('',views.home,name='home')
]
