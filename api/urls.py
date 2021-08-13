from django.urls import path

from api import views

urlpatterns = [
    path('upload/', views.DealFileUploadAPIView.as_view(), name='upload'),
    path('clients/', views.ClientReturnAPIView.as_view(), name='clients'),
]