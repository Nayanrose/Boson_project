from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name='home'),
    
    path('ad',task,name='add'),

    # path('list/',list,name='list'),

    path('add/',Createproject.as_view(),name='add'),

    path('lis1/', listproject.as_view(), name='blg'),

    path('detail/<int:pk>',Detailproject.as_view(),name='detail'),

    path('update/<int:pk>',UpdateView.as_view(),name='update'),

    path('delete/<int:pk>',DeleteView.as_view(),name='delete'),

]
