
# from knox import views as knox_views
from django.urls import path
from demo import views
from .views import *
from .views import delete_user


urlpatterns = [
    path('', views.home,name='home'),
    # path('Studentapi/', views.Studentapi,name='Studentapi'),
   path('users/<int:user_id>/', delete_user, name='delete_user'),
]