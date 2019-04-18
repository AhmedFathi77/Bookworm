
from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from .forms import *
  
# Create your views here. 
def text_image_view(request): 
    if request.method == 'POST': 
        form = TextImgForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return redirect('success') 
    else: 
        form = TextImgForm() 
    return render(request, 'index.html', {'form' : form}) 
  
class success(TemplateView): 
    template_name = 'success.html'
