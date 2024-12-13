from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request,"Input.html")

def output(request):
    name = request.GET["name"]
    password = request.GET["password"]
    return render(request,"Output.html",{"name":name,"password":password})