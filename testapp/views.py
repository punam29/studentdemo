from django.shortcuts import render


from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,"home.html")


@login_required
def java(request):
    return render(request,"java.html")

@login_required
def python(request):
    return render(request,"python.html")

@login_required
def aptitude(request):
    return render(request,"aptitude.html")        


def logout(request):
    return render(request,"logout.html")






