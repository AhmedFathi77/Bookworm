from django import forms 
from .models import TextImg
  
class TextImgForm(forms.ModelForm): 
  
    class Meta: 
        model = TextImg 
        fields = ['name', 'Text_Main_Img'] 