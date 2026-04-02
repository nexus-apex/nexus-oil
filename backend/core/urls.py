from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('wells/', views.well_list, name='well_list'),
    path('wells/create/', views.well_create, name='well_create'),
    path('wells/<int:pk>/edit/', views.well_edit, name='well_edit'),
    path('wells/<int:pk>/delete/', views.well_delete, name='well_delete'),
    path('productions/', views.production_list, name='production_list'),
    path('productions/create/', views.production_create, name='production_create'),
    path('productions/<int:pk>/edit/', views.production_edit, name='production_edit'),
    path('productions/<int:pk>/delete/', views.production_delete, name='production_delete'),
    path('ogequipments/', views.ogequipment_list, name='ogequipment_list'),
    path('ogequipments/create/', views.ogequipment_create, name='ogequipment_create'),
    path('ogequipments/<int:pk>/edit/', views.ogequipment_edit, name='ogequipment_edit'),
    path('ogequipments/<int:pk>/delete/', views.ogequipment_delete, name='ogequipment_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
