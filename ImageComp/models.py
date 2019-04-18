from django.db import models
# Create your models here.
class TextImg(models.Model):
    name = models.CharField(max_length=50) 
    Text_Main_Img = models.ImageField(upload_to='images/') 
