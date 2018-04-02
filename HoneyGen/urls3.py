from django.urls import path

from . import views

urlpatterns = [
	path('generate_otp',views.generate_otp, name='generate_otp'),
	path('verify',views.verify,name='verify')
]