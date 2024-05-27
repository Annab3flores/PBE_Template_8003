from django.urls import path
from .views import feed_empregados, detalhe_empregado, lista_empregados, criar_empregado, editar_empregado, deletar_empregado



urlpatterns = [
    path('', feed_empregados, name='feed_empregados'),
    path('lista/', lista_empregados, name='lista_empregados'),
    path('novo/', criar_empregado, name='criar_empregado'),
    path('editar/<int:pk>/', editar_empregado, name='editar_empregado'),
    path('deletar/<int:pk>/', deletar_empregado, name='deletar_empregado'),
    path('detalhe/<int:pk>/', detalhe_empregado, name='detalhe_empregado'),

]



