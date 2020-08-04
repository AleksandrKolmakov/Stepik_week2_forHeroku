"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import includepip , path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from tours.views import my_custom_page_404
from tours.views import my_custom_page_500
from tours.views import DepartureView
from tours.views import MainView
from tours.views import TourView


urlpatterns = [
    path('', MainView.as_view()),
    path('tour/<int:id>/', TourView.as_view()),
    path('departure/<str:departure>/', DepartureView.as_view()),
]

handler404 = my_custom_page_404
handler500 = my_custom_page_500
