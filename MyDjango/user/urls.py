
from django.urls import path
from . import views
urlpatterns = [
	# 用户登录
	path('login.html', views.loginView, name='login'),
	# 用户注册
	path('register.html', views.registerView, name='register'),
	# 退出登录
	path('logout.html', views.logoutView, name='logout'),
]
