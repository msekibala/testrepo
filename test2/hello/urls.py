from django.urls import path
from. import views
urlpatterns = [
    path('',views.index,name='index'),
    path('mark',views.mark,name="mark"),
    path('<str:name>',views.greet,name='greet'),
]


