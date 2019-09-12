from django.db import models

# Create your models here.
class Duck (models.Model):
   duck_name = models.CharField(max_length=255, help_text='Enter field documentation')
   duck_last_name = models.CharField(max_length=255, help_text='Enter field documentation')
   duck_mail = models.EmailField(max_length=255)
   duck_age = models.IntegerField()

   def __str__(self):
       return self.duck_name