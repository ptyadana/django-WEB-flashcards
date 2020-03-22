from django.urls import path
from flashcard_app import views

urlpatterns = [
   path('',views.home,name='home'),
   path('addition',views.addition,name='addition'),
   path('subtraction',views.subtraction,name='subtraction'),
   path('multiplication',views.multiplication,name='multiplication'),
   path('division',views.division,name='division'),
]
