from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Transacao
from .form import TransacaoForm
import datetime

# Create your views here.

def home(request):

    data = {}

    data['transacoes'] = ['t1', 't2', 't3'] 
    data['now'] = datetime.datetime.now()
    # # html = "<html><body><br>It is %s now.</br></body></html>" % now
    # # return HttpResponse(html)

    return render(request, 'contas/home.html', data)

def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all
    return render(request, 'contas/listagem.html', data)

def nova_transacao(request):
    data = {}
    form = TransacaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'contas/form_novo.html', data)

def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['transacao'] = transacao
    data['form'] = form
    return render(request, 'contas/form.html', data)

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')