from django.shortcuts import redirect, render
from .models import Picture
from .forms import PictureForm

# Necessary for uploads
from cloudinary.forms import cl_init_js_callbacks

# Create your views here.
def index(request):
    pictures = Picture.objects.all()
    ctx = {'pictures': pictures }
    return render(request, 'pictures/index.html', ctx)

def loadPicture(request):
    if request.method == "POST":
        form =  PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    form = PictureForm()
    ctx = {'form': form }
    return render(request, 'pictures/load.html', ctx)