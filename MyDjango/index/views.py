from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from index.models import Product
from .form import *

def index(request):
    if request.method == 'GET':
        product = ProductForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductForm(request.POST)
        if product.is_valid():
            name = product['name']
            cname = product.cleaned_data['name']
            return HttpResponse('提交成功')
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())
def model_index(request, id):
    if request.method == 'GET':
        instance = Product.objects.filter(id=id)
        if instance:
            product = ProductModelForm(instance=instance[0])
        else:
            product = ProductModelForm()
        return render(request, 'data_form.html', locals())
    else:
        product = ProductModelForm(request.POST)
        if product.is_valid():
            weight = product.cleaned_data['weight']
            product_db = product.save(commit=False)
            product_db.name = '我的iPhone'
            product_db.save()
            return HttpResponse('提交成功！weight清洗后的数据为：' + weight)
        else:
            error_msg = product.errors.as_json()
            print(error_msg)
            return render(request, 'data_form.html', locals())

@login_required(login_url='/user/login.html')
@permission_required(perm='index.visit_Product', login_url='/user/login.html')
def index(request):
	return render(request, 'index.html', locals())