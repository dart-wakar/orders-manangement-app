from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^orders/$',views.OrdersList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$',views.OrderDetail.as_view()),
]
