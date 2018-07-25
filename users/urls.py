from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.UserListView.as_view()),
    url('listview',views.ListView.as_view()),
    url(r'api/users', views.UserCreate.as_view(), name='account-create'),

]