from django.shortcuts import render
import requests
from uritemplate import partial
from .models import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.
class Studentapi(viewsets.ModelViewSet):
    queryset=Studentmodel.objects.all()
    serializer_class=Studentserializer
class directorapi(viewsets.ModelViewSet):
    queryset=DirecterDetails.objects.all()
    serializer_class=Directorserializer

class Marksapi(viewsets.ModelViewSet):
    queryset=Marksmodel.objects.all()
    serializer_class=Marksserializer

def home(request):
    # perform business logic
    return render(request, "home.html", {})

#crud
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render 
from .models import Student
from .serializers import Studentserializer



class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentcrudSerilizar(stu)
            return Response(serializer.data)

        stu=Student.objects.all()
        serializer=StudentcrudSerilizar(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=StudentcrudSerilizar(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'}, status=status.
            HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu=Student.objects.get(pk=id)
        serializer=StudentcrudSerilizar(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'compleate data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentcrudSerilizar(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data update'})
        return Response(serializer.errros)

    def delete(self, request,pk,formate=None):
        id=pk
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Date Deleted'})

# nested serizalier foregin key show 
from .serializers import SingerSerilizar
class SingerViewSet(viewsets.ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerilizar

class SongViewSet(viewsets.ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerilizar

# multipe serilizer in same view
from rest_framework.decorators import api_view

@api_view(['GET'])
def showmultiplemodels(request):
    empobj=Employeemodel.objects.all()
    sportobj=Sportsmodel.objects.all()
    singerobj=Singer.objects.all()
    EmpSerializeobj=Employeemodelserializer(empobj,many=True)
    SportsSerializeobj=Sportsmodelserializer(sportobj,many=True)
    SingerSerializeobj=SingerSerilizar(singerobj,many=True)
    Resultmodel=EmpSerializeobj.data + SportsSerializeobj.data + SingerSerializeobj.data
    return Response(Resultmodel)


# code for show html api all data show on html ui page
def showmodels(request):
    resultapi=requests.get('http://127.0.0.1:8000/twomodels')
    jsonobj=resultapi.json()
    return render(request,'index.html',{"employeemodel":jsonobj,"sportsmodel":jsonobj})

# testing payment and order view in one to one


class AlbumViewSet(viewsets.ModelViewSet):
    queryset=Album.objects.all()
    serializer_class=AlbumSerializer
class TrackViewSet(viewsets.ModelViewSet):
    queryset=Track.objects.all()
    serializer_class=TrackSerializer
    
    
class Apicallview(viewsets.ModelViewSet):
    queryset=Apiscall.objects.all()
    serializer_class=APIcallsserializer


# delete user



from django.contrib.auth.models import User
from django.http import JsonResponse

def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully.'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found.'}, status=404)



