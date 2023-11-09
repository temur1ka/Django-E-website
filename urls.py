from django.urls import path, include
from .views import Home,contacts, registration,signin, logoutt
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('logout/', logoutt, name='logout'),
    path('contacts/', contacts, name='contacts'),
    path('register/', registration, name='register'),
    path('login/', signin, name='login'),
    



   

    # path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-sssion'),
   







]