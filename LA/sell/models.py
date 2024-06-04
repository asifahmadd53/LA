from django.db import models
from sell.consts import CITIES,AREAS



class sell(models.Model):
   
    property_action = models.CharField(max_length=10)
    property_type = models.CharField(max_length=20)
    property_subtypes = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    rooms = models.CharField(max_length=5)
    baths = models.CharField(max_length=5)
    name_of_prop = models.CharField(max_length=100)
    additional_details = models.TextField()
    contact_number = models.CharField(max_length=15)
    owner_name = models.CharField(max_length=100)
    availability = models.CharField(max_length=20)
    images = models.ImageField( blank=True, null=True, upload_to="")


    def _str_(self):
        return f'{self.name_of_prop}'