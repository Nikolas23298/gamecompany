from django.shortcuts import render
from django.http import Http404
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView , CreateView , UpdateView
from .models import Game
from django.views.generic.edit import DeleteView 
from django.http.response import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect




class GamesSearchView(LoginRequiredMixin,ListView):
    model = Game
    context_object_name = "games"
    template_name = 'games/games.html'
    login_url = "/login"

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(title__icontains=query).order_by('-types') | Game.objects.filter(types__icontains=query).order_by('-types')
        

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'games/register.html'
    success_url = 'gamelist'

    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('games.list')
        return super().get(request,*args,**kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'games/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'games/login.html'



class GamesDeleteView(DeleteView):
    model = Game
    success_url = '/gamelist'
    template_name = 'games/games_delete.html'


class GamesUpdateView(UpdateView):
    model = Game
    fields = ['title','types','description','age','awards','game_image']
    success_url = '/games/gamelist'


class GamesCreateView(CreateView):
    model = Game
    fields = ['title','types','description','age','awards','game_image']
    success_url = 'gamelist'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class GamesView(TemplateView):
    template_name = 'games/welcome.html'
    extra_context = {'today':datetime.today()}


class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'games/authorized.html'
    login_url ='/admin'


class GamesListView(LoginRequiredMixin,ListView):
    model = Game
    context_object_name = "games"
    template_name = 'games/games.html'
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.games.all()

class GamesDetailView(DetailView):
    model = Game
    context_object_name = "game"


    


