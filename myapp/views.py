from django.shortcuts import render
from myapp.forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        #request.files is bassically for images to save adn we can view it in admin
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request,'home.html',{'form':form,'img':img})
