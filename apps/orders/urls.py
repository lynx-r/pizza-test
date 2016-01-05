from django.conf.urls import url

from .views import OrdersListView, OrderCreateView

urlpatterns = [
    url(r'^$', OrdersListView.as_view(), name='index'),
    url(r'^order/$', OrderCreateView.as_view(), name='order'),
]
