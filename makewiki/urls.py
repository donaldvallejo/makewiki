from django.urls import path
from .views import PageList, PageDetailView

urlpatterns = [
     path('', PageList.as_view(), name='wiki-list-page'),
    
     path('<slug>', PageDetailView.as_view(), name='wiki-details-page'),
]
