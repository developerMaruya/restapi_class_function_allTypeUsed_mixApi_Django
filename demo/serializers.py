# from rest_framework import generics, permissions
from asyncore import read
from rest_framework import serializers
from .models import *


# User Serializer
class Marksserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Marksmodel
        # fields = ('id', 'username', 'email')
        fields="__all__"

class Studentserializer(serializers.ModelSerializer):
    marks=Marksserializer(read_only=True,many=True)
    class Meta:
        model = Studentmodel
        # fields = ('id', 'username', 'email')
        fields="__all__"
class Directorserializer(serializers.ModelSerializer):
    marks=Marksserializer(read_only=True,many=True)
    class Meta:
        model = DirecterDetails

        fields="__all__"
        
# crude
class StudentcrudSerilizar(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']

# nested serialzitaion foregin key 
class PersonSerilizar(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=['id','name','mobile','interests']

class SongSerilizar(serializers.ModelSerializer):
    Person=PersonSerilizar(many=True, read_only=True)
    class Meta:
        model=Song
        fields=['id','title','singer','duration','Person']

class SingerSerilizar(serializers.ModelSerializer):
    sungby=SongSerilizar(many=True, read_only=True)
    # Person=PersonSerilizar(many=True, read_only=True)
    class Meta:
        model=Singer
        fields=['id','name','gender','sungby']

# multiple serilizer in same view looking or one seriliazer
class Employeemodelserializer(serializers.ModelSerializer):
    class Meta:
        model = Employeemodel
        fields="__all__"

class Sportsmodelserializer(serializers.ModelSerializer):
    class Meta:
        model = Sportsmodel
        fields="__all__"

# for one to one payemtn and oreder


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks1 = TrackSerializer(many=True, read_only=True)
    
    

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks1']

class APIcallsserializer(serializers.ModelSerializer):
    class Meta:
        model = Apiscall
        fields="__all__"