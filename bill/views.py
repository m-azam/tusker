from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponseRedirect
from django.urls import reverse
from .models import Category, Subcat, Products
def index(request):
	prod_objs_1 = Products.objects.filter(prod_subcat="1")
	prod_objs_2 = Products.objects.filter(prod_subcat="2")
	prod_objs_3 = Products.objects.filter(prod_subcat="3")
	prod_objs_4 = Products.objects.filter(prod_subcat="4")
	prod_objs_5 = Products.objects.filter(prod_subcat="5")
	prod_objs_6 = Products.objects.filter(prod_subcat="6")
	prod_objs_7 = Products.objects.filter(prod_subcat="7")
	prod_objs_8 = Products.objects.filter(prod_subcat="8")
	prod_objs_9 = Products.objects.filter(prod_subcat="9")
	prod_objs_10 = Products.objects.filter(prod_subcat="10")
	prod_objs_11 = Products.objects.filter(prod_subcat="11")
	prod_objs_12 = Products.objects.filter(prod_subcat="12")
	prod_objs_13 = Products.objects.filter(prod_subcat="13")
	prod_objs_14 = Products.objects.filter(prod_subcat="14")
	prod_objs_15 = Products.objects.filter(prod_subcat="15")
	prod_objs_16 = Products.objects.filter(prod_subcat="16")
	prod_objs_17 = Products.objects.filter(prod_subcat="17")
	prod_objs_18 = Products.objects.filter(prod_subcat="18")
	prod_objs_19 = Products.objects.filter(prod_subcat="19")
	prod_objs_20 = Products.objects.filter(prod_subcat="20")
	prod_objs_21 = Products.objects.filter(prod_subcat="21")
	prod_objs_22 = Products.objects.filter(prod_subcat="22")
	prod_objs_23 = Products.objects.filter(prod_subcat="24")
	prod_objs_24 = Products.objects.filter(prod_subcat="24")
	prod_objs_25 = Products.objects.filter(prod_subcat="25")
	prod_objs_26 = Products.objects.filter(prod_subcat="26")
	return render(request, 'bill/index.html',{'prod_objs_1':prod_objs_1, 'prod_objs_2':prod_objs_2, 'prod_objs_3':prod_objs_3, 'prod_objs_4':prod_objs_4, 'prod_objs_5':prod_objs_5, 'prod_objs_6':prod_objs_6, 'prod_objs_7':prod_objs_7, 'prod_objs_8':prod_objs_8, 'prod_objs_9':prod_objs_9, 'prod_objs_10':prod_objs_10, 'prod_objs_11':prod_objs_11, 'prod_objs_12':prod_objs_12, 'prod_objs_13':prod_objs_13, 'prod_objs_14':prod_objs_14, 'prod_objs_15':prod_objs_15, 'prod_objs_16':prod_objs_16, 'prod_objs_17':prod_objs_17, 'prod_objs_18':prod_objs_18, 'prod_objs_19':prod_objs_19, 'prod_objs_20':prod_objs_20, 'prod_objs_21':prod_objs_21, 'prod_objs_22':prod_objs_22, 'prod_objs_23':prod_objs_23, 'prod_objs_24':prod_objs_24, 'prod_objs_25':prod_objs_25, 'prod_objs_26':prod_objs_26})
def quant(request):
	sel_prod_ids = request.POST.getlist('check[]')
	t_type_val = request.POST["t_type"]
	sel_prod_objs = Products.objects.filter(pk__in=sel_prod_ids)
	if t_type_val == 1:
		return render(request, 'bill/quant.html',{'sel_prod_objs':sel_prod_objs, 't_type_val':t_type_val})
	else
		return render(request, 'bill/quant.html',{'sel_prod_objs':sel_prod_objs})













