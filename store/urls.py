from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name="store"),
    path('store/', views.store, name="store"),
	path('menu/', views.store, name="menu"),
	path('about/', views.about, name="about"),

    path('signup/', views.signup, name="signup"),
	path('Login/', views.Login, name="Login"),
    path('Logout/', views.logout, name="Logout"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/',views.processOrder, name="process_order"),
	path('status/', views.status, name="status"),
	path('register/', views.register, name="register"),
]
