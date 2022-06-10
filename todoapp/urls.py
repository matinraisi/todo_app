from django.urls import path
from . import views


app_name = 'todoapp'

urlpatterns = [
    path('',views.HomeView),
    path('list/',views.todo_list_view , name = 'todo_list'),
    path('creat/',views.totdo_item_creat,name= 'creat_todo'),
    path('<id>/delete',views.delete_todo_item,name= 'delete_item')
]