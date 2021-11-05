from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investments/', views.list, name='list'),
    path('investments/<int:id>/', views.detail, name='detail'),
    path('investments/create/', views.InvestmentCreate.as_view(), name='create_investment'),
    path('investments/<int:pk>/update/', views.InvestmentUpdate.as_view(), name='update_investment'),
    path('investments/<int:pk>/delete.', views.InvestmentDelete.as_view(), name='delete_investment'),
    path('investments/<int:id>/add_prediction/', views.add_prediction, name='add_prediction'),
    path('investments/<int:id>/assoc_source/<int:source_id>', views.assoc_source, name='assoc_source'),
    path('investments/<int:id>/unassoc_source/<int:source_id>', views.unassoc_source, name='unassoc_source'),
    path('sources/', views.SourceList.as_view(), name='list_source'),
    path('sources/create/', views.SourceCreate.as_view(), name='create_source'),
    path('sources/<int:pk>/update/', views.SourceUpdate.as_view(), name='update_source'),
    path('sources/<int:pk>/delete/', views.SourceDelete.as_view(), name='delete_source'),
    path('sources/<int:pk>/', views.SourceDetail.as_view(), name='source_detail'),
]