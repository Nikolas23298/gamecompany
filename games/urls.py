from django.urls import path
from . import views 

urlpatterns = [
    path('', views.GamesView.as_view(), name="home"),
    path('authorized',views.AuthorizedView.as_view()),
    path('gamelist',views.GamesListView.as_view(), name="games.list"),
    path('gamedetail/<int:pk>/',views.GamesDetailView.as_view(), name="games.detail"),
    path('gamedetail/<int:pk>/edit',views.GamesUpdateView.as_view(), name="games.update"),
    path('gamedetail/<int:pk>/delete/',views.GamesDeleteView.as_view(), name="games.delete"),
    path('new', views.GamesCreateView.as_view(), name = "games.new"),
    path('login', views.LoginInterfaceView.as_view(), name = "login"),
    path('logout', views.LogoutInterfaceView.as_view(), name = "logout"),
    path('signup',views.SignupView.as_view(), name = "signup"),
    path('search-results',views.GamesSearchView.as_view(), name="search.results"),
]