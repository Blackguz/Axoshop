
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('entrada', views.entrada, name='entrada'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('comunidad', views.comunidad, name='comunidad'),
    path('tienda', views.tienda, name='tienda'),
    path('producto/<int:id>/', views.producto, name='producto'),
    path('lobby', views.lobby, name='lobby'),
]