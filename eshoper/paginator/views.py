from django.shortcuts import render, redirect
from .models import Create, CreateItem
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView,  TemplateView



def list_creates(request):
    create_list = Create.objects.all()
    paginator = Paginator(create_list, 2 )  # Show 25 contacts per page.
    items=CreateItem.objects.filter(user=request.user)
    total = sum(1 * item.quantity for item in items)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "shop.html", {"create_list":create_list, "page_obj": page_obj, 'total': total})
# Create your views here.



def view_cart(request):
	cart_items = CreateItem.objects.filter(user=request.user)
	total_price = sum(item.create.price * item.quantity for item in cart_items)
	return render(request, 'paginator/sabad.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product_id = Create.objects.get(id=product_id)
    cart_item = CreateItem.objects.filter(user=request.user, create=product_id).first()

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, "Cart updated!")
    else:
        CreateItem.objects.create(user=request.user, create=product_id)
        messages.success(request, "your Cart updated!")

    return redirect('paginator:view_cart')

def remove_from_cart(request, item_id):
    cart_item = CreateItem.objects.get(id=item_id)

    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")

    return redirect("paginator:view_cart")

def home(request):
    return HttpResponse('Hello, World!')

class SearchResultsView(ListView):
    model = Create
    template_name = 'paginator/search.html'
    context_object_name = 'creats'


    def get_queryset(self):
        query = self.request.GET.get("S")
        if query:
           creats=Create.objects.filter(Q(name__icontains=query) | Q(made_in__icontains=query) | Q(price__icontains=query))
           return creats
