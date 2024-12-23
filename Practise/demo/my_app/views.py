from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
# Create your views here.           # new line
def Home(request):
    if request.method == "POST":
        Name = request.POST["name"]
        Age = request.POST["age"]
        Address = request.POST["address"]
        Contact = request.POST["contact"]
        Email = request.POST["email"]

        obj = Datas()
        obj.Name = Name
        obj.Age = Age
        obj.Address = Address
        obj.Contact = Contact
        obj.Email = Email
        obj.save()
    return render(request,"Home.html")

def Index(request):
    msg = "<h1>Hello this is index page</h1>"
    return HttpResponse(msg)

def User(request):
    return render(request,"user.html")

def Image(request):
    return render(request,"Img.html")

def Bootstrap(request):
    return render(request,"Bootstrap.html")