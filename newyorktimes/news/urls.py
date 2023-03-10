from django.urls import path

from .views import *

urlpatterns = [
    path('', NewsView.as_view(), name='home' ),
    path('details_news/<int:pk>', NewsDetails.as_view(), name='details_news')
]