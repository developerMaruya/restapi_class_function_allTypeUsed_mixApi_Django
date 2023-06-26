import email
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.
class Studentmodel(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=100)

    total_present=models.IntegerField()
    qualification=models.CharField(max_length=100)
    behavior=models.CharField(max_length=100)

class EmployeeDetails(models.Model):
    empid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    you_check_it=models.BooleanField(default=True)

class DirecterDetails(models.Model):
    dirid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)

class Marksmodel(models.Model):
    Marksid=models.IntegerField(primary_key=True)
    maths=models.IntegerField()
    physics=models.IntegerField()
    computers=models.IntegerField()
    stid=models.ForeignKey(Studentmodel,related_name='marks',on_delete=models.CASCADE)
    # empid=models.ForeignKey(EmployeeDetails,related_name='emp',on_delete=models.CASCADE)
    # EmployeeDetail = models.ManyToManyField(EmployeeDetails)
    # directorDetail = models.ManyToManyField(DirecterDetails)
    EmployeeDetail = models.ForeignKey(EmployeeDetails, related_name='EmployeeDetail', on_delete=models.CASCADE, null=True, blank=True)
    directorDetail = models.ForeignKey(DirecterDetails, related_name='directorDetail', on_delete=models.CASCADE, null=True, blank=True)



#crud operation api
from django.db import models
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)

# one to one vs one to many vs many to many
from django.contrib.auth.models import User
#one to one
class UserInterface1(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='userpoint')
    age=models.PositiveSmallIntegerField()
    note=models.CharField(max_length=244)

    def __str__(self):
        return self.user.username
# foreign key
class UserInterface2(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='userpoint2')
    age=models.PositiveSmallIntegerField()
    note=models.CharField(max_length=244)

    def __str__(self):
        return self.user.username
# many to many
class UserInterface3(models.Model):
    user=models.ManyToManyField(User,related_name='userpoint3')
    age=models.PositiveSmallIntegerField()
    note=models.CharField(max_length=244)

# mix up all foregin key to each other
class Intrest(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title
class City(models.Model):
    title=models.CharField(max_length=200)

    def __str__(self):
        return self.title
# use many to many
class Person(models.Model):
    name=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    interests=models.ManyToManyField(Intrest)

    def __str__(self):
        return self.name
# foreigin key and one to one use both
class PersonAddress(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    city=models.ForeignKey(City, on_delete=models.CASCADE)
    street_address=models.CharField(max_length=244)
    # mobile=models.OneToOneField(Person, on_delete=models.CASCADE)
    interests=models.ManyToManyField(Intrest)

    def __str__(self):
        # return self.person.name + "{" + self.street_address + "}"+  self.mobile + "}"+  self.city.title + "}"
        return self.person.name + "{" + self.street_address +"  , "+self.person.mobile+ "}"


# nested serilizer 
class Singer(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

class Song(models.Model):
    title=models.CharField(max_length=244)
    singer=models.ForeignKey(Singer, on_delete=models.CASCADE,related_name='sungby')
    Person = models.ManyToManyField(Person)
    duration=models.IntegerField()

    def __str__(self):
        return self.title

# multiple serializer in same view 
class Employeemodel(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    salary=models.CharField(max_length=150)

    class Meta:
        db_table="employee"

class Sportsmodel(models.Model):
    sportid=models.IntegerField(primary_key=True)
    sportname=models.CharField(max_length=150)
    sporttimeing = models.CharField(max_length=150)


    class Meta:
        db_table="sports"

# testing for payment one to one
class Payment(models.Model):
    # id=models.IntegerField(primary_key=True)
    id=models.AutoField(primary_key=True)
    amount = models.IntegerField()
    type=models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)
class Order(models.Model):
    id=models.AutoField(primary_key=True)
    qty=models.IntegerField()
    # payment = models.ManyToManyField(Payment,related_name='order') 
    payment=models.OneToOneField(Payment, on_delete=models.CASCADE,related_name='payment', null=True, blank=True)
    
    def __str__(self):
        return str(self.id)

#testing django oficeal docu
class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks1', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)

        
# api with flutter calling and testing

class Apiscall(models.Model):
    slug=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=100)



    


    
