from django.shortcuts import redirect, render
from marketplace.models import Marketplaces
from marketplace.form import MarketplaceForm


# Create your views here.
def marketplaces(request):
    data = {}
    data['db'] = Marketplaces.objects.all()
    return render(request, 'marketplace.html', data)


# Formulario de Marketplaces (reaproveitamento para CREATE e UPDATE)
def marketplacesForm(request):
    data = {}
    data['formMarketplaces'] = MarketplaceForm()
    return render(request, 'marketplacesForm.html', data)


# Função que cria um novo Marketplace (CREATE)
def createMarketplaces(request):
    form = MarketplaceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/marketplace')


# Função que lê um Marketplace existente (READ)
def viewMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    return render(request, 'viewMarketplace.html', data)


# Função que edita um Marketplace existente (UPDATE)
def editMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    data['formMarketplaces'] = MarketplaceForm(instance=data['db'])
    return render(request, 'marketplacesForm.html', data)


# Função que atualiza um Marketplace existente (UPDATE)
def updateMarketplace(request, pk):
    data = {}
    data['db'] = Marketplaces.objects.get(pk=pk)
    form = MarketplaceForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/marketplace')


# Função que deleta um Marketplace existente (DELETE)
def deleteMarketplace(request, pk):
    db = Marketplaces.objects.get(pk=pk)
    db.delete()
    return redirect('/marketplace')
    # return render (request, 'marketplace.html')
