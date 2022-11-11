from django.urls import path
from .views import *

urlpatterns=[
    path('', CategoryListView.as_view(), name='categ'),
    path('firm/<int:id>/', FirmListView.as_view(), name='firm'),
    path('firm/history/<int:id>/', FirmDetailView.as_view(), name='firm_detail'),

]