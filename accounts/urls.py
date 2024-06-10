from django.urls import path

from .views import signup ,user_activate ,dashboard ,resend_activation_code

urlpatterns = [
    path('signup' , signup , name='signup'),
    path('activate/<str:username>/',user_activate ,name='user_activate'),
    path('resend-code/<str:username>/',resend_activation_code, name='resend_code'),



    path('dashboard' , dashboard),


]