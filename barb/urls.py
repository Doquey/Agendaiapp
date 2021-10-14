from django.urls import path
from . import views
app_name="barb"
urlpatterns =[
    path('',views.index,name="index"),
    path('contatos/', views.contatos, name="contatos"),
    path('agenda/', views.agenda, name="agenda"),
    path('informaçoes/',views.informaçoes, name="info"),
    path('reservas/',views.reservas,name="reservas"),
    path('carrinho/', views.carrinho,name="carrinho")
]