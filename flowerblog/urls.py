from django.urls import path
from .views import home, about, contact

urlpatterns = [
    path('', home, name='flowerblog-home'),
    path('about/', about, name='flowerblog-about'),
    path('contact/', contact, name='flowerblog-contact'),
]

