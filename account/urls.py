from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('singup/',views.Singup_view,name='singup'),
     path('login/',views.Login_view,name='login'),
     path('logout/',views.Logout_view,name='logout'),

]