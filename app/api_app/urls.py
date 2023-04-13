from django.urls import path

from api_app.views import json_add_number, get_token_view

urlpatterns = [
    path('add/', json_add_number, name='add'),
    path('token/', get_token_view, name='token'),
]
