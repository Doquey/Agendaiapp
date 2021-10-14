from django.shortcuts import render

def index(request):
    return render(request,'barb/index.html')

def contatos(request):
    return render(request,'barb/contatos.html')

def informaçoes(request):
    return render(request,"barb/informacoes.html")

def agenda(request):
    return render(request,"barb/agenda.html")


def reservas(request):
    return render(request,'barb/reservas.html')

def carrinho(request):
    return render(request,'barb/carrinho.html')