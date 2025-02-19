from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.from django.shortcuts import render

# Create your views here.
def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/lists/the-only-list-in-the-world/")

    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

def view_list(request):
    items = Item.objects.all()
    return render(request, "home.html", {"items": items})

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST["item_text"], list=our_list)
    return redirect(f"/lists/{our_list.id}/")
