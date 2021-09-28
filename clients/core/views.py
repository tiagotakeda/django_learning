from django import http
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Client
from .form import ClientForm

def home(request):
    valores = [0, 1, 2, 3, 4, 5, 6, 7]
    restos = []

    for i in valores:
        if valores.index(i) % 2 == 0:
            restos.append(i)
    
    return render(request, 'home.html', {'valores': valores, 'restos': restos})

def articles(request, year):
    return HttpResponse('<b>Returning articles from %s</b>' % year)

def hello(request, name, age):
    return HttpResponse('Hello %s, you are %s' % (name, age))

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def new_client(request):
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'form_new.html', {'form': form})

def update_client(request, id):
    client = get_object_or_404(Client, pk=id)
    form = ClientForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect(list_clients)

    return render(request, 'form.html', {'form': form, 'client': client})

def delete_client(request, id):
    client = get_object_or_404(Client, pk=id)

    if request.method == 'POST':
        client.delete()
        return redirect(list_clients)

    return render(request, 'confirm.html', {'client': client})