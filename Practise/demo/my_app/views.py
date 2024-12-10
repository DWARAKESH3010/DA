from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.           # new line
def Home(request):
    return render(request,"Home.html")

def Index(request):
    msg = "<h1>Hello this is index page</h1>"
    return HttpResponse(msg)

def User(request):
    return render(request,"user.html",{"Name":"dwara"})