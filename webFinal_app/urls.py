from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomePageView, SearchResultsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('a/', views.carA, name='a'),
    path('b/', views.carB, name='b'),
    path('c/', views.carC, name='c'),
    path('e/', views.carE, name='e'),
    path('s/', views.carS, name='s'),
    path('m/', views.carM, name='M'),
    path('amg/', views.carAMG, name='amg'),
    path('gls/', views.carGLS, name='gls'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('feedbacc/', views.leave_feedback, name='f'),
    path('car/', views.ShowCarView.as_view(), name='car'),

]
