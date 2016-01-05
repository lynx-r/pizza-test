from django.views.generic import TemplateView, FormView, CreateView, ListView
from .models import Order

from .form import OrderForm


class OrdersListView(ListView):
    template_name = 'orders/index.html'
    queryset = Order.objects.all()
    context_object_name = 'order_list'


class OrderCreateView(CreateView):
    template_name = 'orders/form.html'
    form_class = OrderForm
    success_url = '/'
