"""demodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
# from django.db import router
from django.urls import path,include
from demo import views
# from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("Studentmodel",views.Studentapi),
router.register("Marksmodel",views.Marksapi)
router.register("directmodel",views.directorapi)

#for multiple table data show in one view
# router.register("singer",views.SingerViewSet)
# router.register("song",views.SongViewSet)


router.register("AlbumSerializer",views.AlbumViewSet)
router.register("track",views.TrackViewSet)
router.register("callapi",views.Apicallview)
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/',include(router.urls)),
    path('',include('demo.urls')), 

    path('studentapi/',views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.StudentAPI.as_view()),

    path('twomodels',views.showmultiplemodels),
    path('apiindex/',views.showmodels)
    


]

