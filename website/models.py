from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    KRA_PIN = models.CharField(max_length=11)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")


    

