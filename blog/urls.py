from django.urls import path
from . import views
#Djangoのpath と blogアプリのすべてのビューをインポートする

urlpatterns = [
    path('',views.post_list, name='post_list'),
]


