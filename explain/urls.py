from django.urls import path, include
from explain.views import process_explain

urlpatterns = [
    path('', process_explain)
]