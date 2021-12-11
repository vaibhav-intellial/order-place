from datetime import datetime
from re import I, M

from django.contrib import admin
from django.db.models.fields.related import ForeignKey
from django.shortcuts import HttpResponseRedirect, redirect, render

from .models import Order, OrderItem, Product

# Create your views here.


def form(request):
    # home page
    topproduct = Product.objects.values("name", "id").order_by("-id")[0:10]

    return render(
        request,
        "form.html",
        {
            "topproduct": topproduct,
        },
    )


def add_deatil(request):
    # html file to data collect

    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    address_street = request.POST["address_street"]
    address_landmark = request.POST["address_landmark"]
    address_pincode = request.POST["address_pincode"]
    product = request.POST["product"]
    quantity = request.POST["quantity"]
    prize = request.POST["prize"]

    addordermodel = Order.objects.create(
        firstname=firstname, lastname=lastname, email=email, address_street=address_street, address_landmark=address_landmark, address_pincode=address_pincode
    )
    addorderitemmodel = OrderItem.objects.create(product_id=product, order_id=addordermodel.id, quantity=quantity, prize=prize)

    allproduct = Product.objects.all()
    sms = "Order Done!"

    return render(request, "form.html", {"sms": sms, "allproduct": allproduct})


def all_deatil(request):

    allorderitem = OrderItem.objects.all()

    return render(request, "alldata.html", {"allorderitem": allorderitem})


def delete_deatil(request, id):
    # delete order
    allorderitem = OrderItem.objects.filter(order_id=id)
    allorderitem.delete()

    return redirect("all_deatil")


def edit_deatil(request, id):
    # edit order data
    allorderitem = OrderItem.objects.get(order_id=id)
    topproduct = Product.objects.values("name", "id").order_by("-id")[0:10]
    editsms = "Edit Order!"

    return render(request, "editdata.html", {"allorderitem": allorderitem, "topproduct": topproduct, "editsms": editsms})


def update_deatil(request, id):
    # order update deatil
    allorderitem = OrderItem.objects.get(order_id=id)
    allordermodel = Order.objects.get(orderitem=allorderitem)
    allproduct = Product.objects.all()

    # data collect template side
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    email = request.POST.get("email")
    address_street = request.POST.get("address_street")
    address_landmark = request.POST.get("address_landmark")
    address_pincode = request.POST.get("address_pincode")
    product = request.POST.get("product")
    quantity = request.POST.get("quantity")
    prize = request.POST.get("prize")

    # save data model (updated data)
    allordermodel.firstname = firstname
    allordermodel.lastname = lastname
    allordermodel.email = email
    allordermodel.address_street = address_street
    allordermodel.address_landmark = address_landmark
    allordermodel.address_pincode = address_pincode
    allorderitem.product_id = product
    allorderitem.quantity = quantity
    allorderitem.prize = prize
    allorderitem.created_on = datetime.now()

    allordermodel.save()
    allorderitem.save()

    allorderitem = OrderItem.objects.all()
    msg = "save change!"

    return render(request, "alldata.html", {"allorderitem": allorderitem, "allproduct": allproduct, "msg": msg})
