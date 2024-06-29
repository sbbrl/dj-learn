from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    # path('educative/',views.educative,name="educative"),
    path('<int:num>/',views.even_or_odd,name = "even_or_odd"),
    # path('<age>/',views.show_age,name = "show_age"),
    path('admin/', admin.site.urls),
]
