from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('all-news/', views.all_news, name='all_news'),
    path('news/<int:pk>/', views.read_news, name='read_news'),
    path('category/<int:pk>/', views.news_by_category, name='category_news'),
    path('search/', views.search, name='search'),
    path('register/', views.register_view, name='register'), # register_view емес, register
    path('login/', views.login_view, name='login'),          # login_viewn емес, login
    path('logout/', views.logout_view, name='logout'),       # logout_view емес, logout
]