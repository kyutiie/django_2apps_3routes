
from django.urls import path
from .views import flowerallpink,flowerrose, flowertulips

urlpatterns = [
    path('', flowerallpink, name='flowerexamples-flowerallpink'),  # Root example
    path('flowerrose/', flowerrose, name='flowerexamples-flowerrose'),  # Second example
    path('flowertulips/', flowertulips, name='flowerexamples-flowertulips'),  # Third example
]
