from django.urls import path

from api_app.views import json_add_number, get_token_view, json_subtract_number, json_multiply_number, json_divide_number

urlpatterns = [
    path('add/', json_add_number, name='add'),
    path('token/', get_token_view, name='token'),
    path('subtract/', json_subtract_number, name='subtract'),
    path('multiply/', json_multiply_number, name='multiply'),
    path('divide/', json_divide_number, name='divide'),
]
