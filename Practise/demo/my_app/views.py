from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.           # new line
def Home(request):
    return render(request,"Home.html")

def Index(request):
    msg = "<h1>Hello this is index page</h1>"
    return HttpResponse(msg)

def User(request):
    mobile = request.GET["mobile"]
    Keyboard = request.GET["Keyboard"]
    monitor = request.GET["monitor"]
    price = int(mobile) + int(Keyboard) + int(monitor)
    return render(request,"user.html",{"price":price})

def Image(request):
    return render(request,"Img.html")

def Bootstrap(request):
    return render(request,"Bootstrap.html")