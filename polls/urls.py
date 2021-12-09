from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index, name='index'),
    #path('<int:poll_id>/', views.detail, name='detail'),
    #path('<int:poll_id>/results/', views.results, name='results'),
    path('create/', views.create, name='create'),
    path('read/<int:id>', views.read, name='read'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
