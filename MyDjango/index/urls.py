from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # path('login.html', views.login),
    # path('index/', views.ProductList.as_view()),
    # path('index/<id>.html', views.ProductList.as_view(), {'name': 'phone'})
    path('<int:id>.html', views.model_index),

]