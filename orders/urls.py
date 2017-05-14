from django.conf.urls import url
from orders import views

urlpatterns = [
    url(r'^orders/$',views.OrdersList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$',views.OrderDetail.as_view()),
    url(r'^orders/create/$',views.OrderCreate.as_view()),
    url(r'^orders/edit/$',views.OrderEdit.as_view()),
    url(r'^orders/delete/$',views.OrderDelete.as_view()),
    url(r'^orders/list/$',views.OrderListRetrieve.as_view()),
    url(r'^users/register/$',views.UserRegister.as_view()),
    url(r'^users/$',views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view()),
    url(r'^users/delete/$',views.UserDelete.as_view()),
]
