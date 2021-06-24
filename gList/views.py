from django.shortcuts import render
from .forms import AddItemForm
from .models import GItem
from django.http import HttpResponseRedirect
# Create your views here.
def home_view(request, *args):
    return render(request, "index.html", {"items":GItem.objects.all()})

def add_view(request, *args):

    if request.method=="POST":
        form = AddItemForm(request.POST)
        
        if form.is_valid():
            item_name = form.cleaned_data["item_name"]
            item_qty = form.cleaned_data["item_qty"]
            item_status = form.cleaned_data["item_status"]
            items = GItem.objects.create(
                user=request.user.get_username(),
                item_name=item_name,
                item_qty=item_qty,
                item_status=item_status
            )
            items.save()

            return HttpResponseRedirect('/')

    return render(request, "add.html", {'form': AddItemForm()})

def update_view(request,id , *args):
    return HttpResponseRedirect('/')


def del_view(request, id,*args):
    GItem.objects.all().get(id=id).delete()
    return HttpResponseRedirect('/')