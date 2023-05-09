from django.contrib import admin
from django.urls import path
from Mywebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('addnews',views.addnews),
    path('result',views.result,name="result"),
]
