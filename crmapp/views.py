from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def dashboard(request):
    return render(request,'dashboard.html')

def archive(request):
    return render(request,'archive.html')