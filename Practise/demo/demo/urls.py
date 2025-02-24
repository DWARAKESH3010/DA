"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app.views import Home,Index,User,Image,Bootstrap,Add_data,Updatedata,DeleteData,Back
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name="Home"),  # new Line
    path("Add_data",Add_data,name="Add_data"),
    path("UpdateData/<int:id>",Updatedata,name = "Updatedata"),
    path('Back',Back, name="Back"),
    path("DeleteData/<int:id>",DeleteData,name = "DeleteData"),
    path("Index/",Index), #new Line
    path("User/",User),
    path("Img/",Image),
    path("Boot/",Bootstrap)
]
