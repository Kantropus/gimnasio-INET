from django.db import models
from django.db.models.deletion import PROTECT
# Create your models here.
class GimRoom(models.Model):
    """Data for each room of the gim."""
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=45)
    area = models.IntegerField()
    room_type = models.CharField(max_length=45)
    def __str__(self) -> str:
        return f"{self.room_type} {self.location}" 

class GimLesson(models.Model):
    """Data for the gim lessons."""
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=60)
    datetime = models.DateTimeField()
    room = models.ForeignKey(GimRoom, on_delete=PROTECT, default=None)

    def __str__(self) -> str:
        return self.description

class GimTeacher(models.Model):
    """Data of each gim teacher."""
    dni = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    phone_number = models.PositiveBigIntegerField()
    hiring_date = models.DateField()
    birthdate = models.DateField()
    
class GimClient(models.Model):
    affiliate_number = models.IntegerField(primary_key=True)
    profession = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.TextField(max_length=45)
    phone_number = models.PositiveBigIntegerField()
    is_up_to_date = models.BooleanField()