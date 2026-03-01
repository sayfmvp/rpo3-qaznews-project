from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Ad
import random
from django.shortcuts import render, get_object_or_404, redirect # redirect қосылды
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .models import Post, Category, Ad
import random

def index(request):
    # Соңғы 4 жазба
    latest_posts = Post.objects.all().order_by('-created_at')[:4]
    # Кездейсоқ 6 жазба
    all_posts = list(Post.objects.all())
    random_posts = random.sample(all_posts, min(len(all_posts), 6))
    # Соңғы 4 жарнама
    ads = Ad.objects.all().order_by('-id')[:4]
    
    return render(request, 'index.html', {
        'latest_posts': latest_posts,
        'random_posts': random_posts,
        'ads': ads
    })

def all_news(request):
    posts = Post.objects.all().order_by('-created_at')
    ads = Ad.objects.all().order_by('-id')[:4]
    return render(request, 'all-news.html', {'posts': posts, 'ads': ads})

def read_news(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Санат бойынша ұқсас 4 жазба (Бонус)
    related_posts = Post.objects.filter(category=post.category).exclude(pk=pk)[:4]
    return render(request, 'read-news.html', {'post': post, 'related_posts': related_posts})

def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk) # Санатты ID бойынша табу
    posts = Post.objects.filter(category=category).order_by('-created_at') # Сол санаттағы посттарды сүзу
    return render(request, 'news-by-category.html', {
        'category': category,
        'posts': posts
    })
def search(request):
    query = request.GET.get('q') # Формадан 'q' айнымалысын алу
    if query:
        # Тақырыбы немесе мәтіні бойынша іздеу
        results = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    else:
        results = []
    
    return render(request, 'search_results.html', {'results': results, 'query': query})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.is_staff = True  <- Бұл жерді абайлап қолданыңыз
            login(request, user)
            return redirect('home') # 'index' емес, 'home' (urls.py-дағы name бойынша)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') # Осы жер дұрыс
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Жүйеден шығу
def logout_view(request):
    logout(request)
    return redirect('home')