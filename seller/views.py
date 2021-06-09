from django.shortcuts import redirect, render
from seller.models import Seller
from .form import SellerForm


def home(request):
    return render(request, 'base.html')

def seller(request):
    data = {}
    data['db'] = Seller.objects.all()
    return render(request, 'seller.html', data)

def seller_form(request):
    data = {}
    data['seller_form'] = SellerForm()
    return render(request, 'seller_form.html', data)

def create_seller(request):
    form = SellerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/seller')

def view_seller(request, pk):
    data = {}
    data['db'] = Seller.objects.get(pk=pk)
    return render(request, 'seller', data)

def edit_seller(request, pk):
    data = {}
    data['db'] = Seller.objects.get(pk=pk)
    data['seller_form'] = SellerForm(instance=data['db'])
    return render(request, 'seller_form.html', data)

def update_seller(request, pk):
    data = {}
    data['db'] = Seller.objects.get(pk=pk)
    form = SellerForm(request.POST or None, instance=data['db'])

    if form.is_valid():
        form.save()
        return redirect('seller')

def delete_seller(pk):
    seller = Seller.objects.get(pk=pk)
    seller.delete()
    return redirect('seller')

