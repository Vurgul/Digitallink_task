from django.urls import path

from . import views
# Строка для работы namespace
app_name = 'links'

urlpatterns = [
    path('api/links/', views.GetLinkInfoView.as_view()),
    # Главная страница
    path('', views.index, name='index'),
    # Список постов групп
    path(
        '<str:slug>',
        views.number,
        name='numbers'
    ),

]
