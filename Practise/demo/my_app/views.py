from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
# Create your views here.           # new line
def Home(request):
    my_data = Datas.objects.all()
    if my_data != "":
        return render(request,"Home.html",{"datas":my_data})
    else:
        return render(request,"Home.html")

def Add_data(request):
    if request.method == "POST":
        Name = request.POST.get("name", "")
        Age = int(request.POST.get("age", 0))
        Address = request.POST.get("address", "")
        Contact = int(request.POST.get("contact", 0))
        Email = request.POST.get("email", "")

        try:
            obj = Datas(Name=Name, Age=Age, Address=Address, Contact=Contact, Email=Email)
            obj.save()
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")

        
        return redirect("Home")  


    my_data = Datas.objects.all()
    return render(request, "Home.html", {"datas": my_data})

def Updatedata(request):
    
    return render(request,"Update.html")
    
def Index(request):
    msg = "<h1>Hello this is index page</h1>"
    return HttpResponse(msg)

def User(request):
    return render(request,"user.html")

def Image(request):
    return render(request,"Img.html")

def Bootstrap(request):
    return render(request,"Bootstrap.html")