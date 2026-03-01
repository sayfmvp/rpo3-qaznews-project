from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all-news/', views.all_news, name='all_news'),
    path('news/<int:pk>/', views.read_news, name='read_news'),
    path('category/<int:pk>/', views.news_by_category, name='category_news'),
    path('search/', views.search, name='search'),
    path('register/', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_viewn'),
    path('logout/', views.logout_view, name='logout_view'),
]
