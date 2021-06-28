from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Orders,OrderUpdate
import json
from django.views.decorators.csrf import csrf_exempt
from math import ceil
def home(request):

    allproduct=[]
    catproduct=Product.objects.values('category','id')
    cats={item['category'] for item in catproduct}
    for cat in cats:

        prod=Product.objects.filter(category=cat)

        n=len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allproduct.append([prod,range(1,nslides),nslides])

    # nslides=n//4+ceil((n/4)-(n//4))
    # allproduct=[[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    # params={'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    params={'allproduct':allproduct}
    return render(request,'shop/indexshop.html',params)
def contact(request):
    res=False
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        print(name,email,phone, desc )

        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        res=True
        return render(request, "shop/contact.html",{"res":res})
    return render(request, "shop/contact.html")
def abouts(request):
    return render(request,'shop/abouts.html')
def tracker(request):
    if request.method=="POST":
         orderId = request.POST.get('orderId', '')
         email = request.POST.get('email', '')

         try:
             order=Orders.objects.filter(order_id=orderId,email=email)
             if len(order)>0:
                 update=OrderUpdate.objects.filter(order_id=orderId)
                 updates=[]
                 for item in update:
                     updates.append({'text':item.update_desc,'time':item.timestamp})
                     response=json.dumps([updates,order[0].items_json], default=str)
                 return HttpResponse(response)
             else:
                 return HttpResponse("{}")
         except Exception as e:
            return HttpResponse("{}")

    return render(request,'shop/tracker.html')
def search(request):
    return HttpResponse("this is for searching this is the page of  ")
def prodview(request,id):
    product = Product.objects.filter(id=id)

    return render(request,'shop/productview.html',{'product':product[0]})
def checkout(request):
    if request.method=="POST":
        print(request)
        items_json=request.POST.get('itemsJson', '')
        amount=request.POST.get('amount', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '')+" "+request.POST.get('address2','')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order=Orders(items_json=items_json,name=name, email=email, address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="The order has been placed")
        update.save()
        thank = True
        id =order.order_id
        return render(request,'shop/Checkout.html',{'thank':thank,'id':id})
    #        request paytm to transfer the amount to your account after payment by user
    
    return render(request,'shop/Checkout.html')
@csrf_exempt
def handlerequest(request):
#     paytm will send you post request here
      pass
