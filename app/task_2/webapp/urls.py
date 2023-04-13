from django.urls import path

from webapp.views import Index

urlpatterns = [
    path('index/', Index.as_view(), name='index'),
]
