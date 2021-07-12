from django.urls import path
from .views import SnackView,SnackDetailsView
urlpatterns=[
path('', SnackView.as_view(), name='Snacks'),
path('<int:pk>/', SnackDetailsView.as_view(), name='snack_details'),

]
