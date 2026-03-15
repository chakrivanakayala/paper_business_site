from django.shortcuts import render
from orders.models import PaperOrder

def home(request):
    message = ""
    if request.method == "POST":
        name = request.POST.get('customer_name')
        p_type = request.POST.get('paper_type')
        qty = request.POST.get('quantity')

        new_order = PaperOrder(customer_name=name, paper_type=p_type, quantity=qty)
        new_order.save()
        return render(request, 'success.html', {'name': name})

    # DATABASE NUNDI ORDERS ANNI TISKOVADAM
    all_orders = PaperOrder.objects.all().order_by('-order_date') # Kotha orders paina kanipisthayi
    
    return render(request, 'index.html', {'orders': all_orders})