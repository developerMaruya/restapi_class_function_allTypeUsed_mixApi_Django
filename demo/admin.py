from django.contrib import admin
from .models import *

# Register your models here.
class MarksmodelAdmin(admin.ModelAdmin):
    list_display=('Marksid','stid','EmployeeDetail','directorDetail',)
    list_per_page=5
    
admin.site.register(Studentmodel)
admin.site.register(Marksmodel,MarksmodelAdmin)
admin.site.register(EmployeeDetails)
admin.site.register(DirecterDetails)
admin.site.register(Apiscall)

#crud
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','city']
# under standing one to one vs foreign key vs many to many
admin.site.register(UserInterface1)
admin.site.register(UserInterface2)
admin.site.register(UserInterface3)

# foreign key and many to many woring with same (all realation)
admin.site.register([Intrest,City,Person,PersonAddress])

# nested serilization used in foregen key 
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id','name','gender']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['id','title','singer','duration']

# multiple serilizer in same view
admin.site.register([Employeemodel,Sportsmodel])
#testing for one to one

admin.site.register([Album,Track])
