from django.shortcuts import redirect, render
from seller.models import Seller
from .form import SellerForm


# Create your views here.
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
        return redirect('seller')
    return render(request, 'seller_form.html', {'form':form})

def list_seller(request, id):
    data = {}
    data['db'] = Seller.objects.all(id=id)
    return render(request, 'seller.html', data)

def update_seller(request, id):
    data = {}
    data['db'] = Seller.objects.get(id=id)
    form = SellerForm(request.POST or None, instance=data['db'])

    if form.is_valid():
        form.save()
        return redirect('seller')
    return render(request, 'seller_form.html', {'form':form, 'seller':seller})

def delete_seller(request, id):
    seller = Seller.objects.get(id=id)
    seller.delete()
    return redirect('seller')

