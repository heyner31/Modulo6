from django.urls import path
from .views import CoreHome

app_name = 'core'
urlpatterns = [
    path('', CoreHome.as_view(), name='home'),
]
