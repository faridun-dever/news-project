from django.shortcuts import render, redirect
from .models import Category, Article
from .forms import UserRegiserForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout


def index(request):
    title = "News Blog | Homepage"
    articles = Article.objects.all().order_by('-created').values()
    categories = Category.objects.all().order_by("name").values()
    return render(request, 'index.html', {
        "title": title,
        "articles": articles,
        "categories": categories
    })


def blog(request, article_id):
    article = Article.objects.get(id=article_id)
    category = article.category
    articles = Article.objects.filter(category_id=category.id)
    title = f"News Blog | {article.title}"
    return render(request, 'blog.html', {
        "title": title,
        "article": article,
        "category": category,
        "articles": articles,
    })


def about(request):
    title = "About us | Best news"
    return render(request, "about.html", {
        "title": title
    })


def get_category(request, category_id):
    categories = Category.objects.all().order_by("name").values()
    articles = Article.objects.filter(category_id=category_id)
    category = Category.objects.get(id=category_id)
    title = f"News Blog | {category.name}"
    return render(request, "category.html", {
        "categories": categories,
        "articles": articles,
        "category": category,
        "title": title
    })


def loginauth(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {"form": form})


def signup(request):
    if request.method == "POST":
        form = UserRegiserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "The account has been created successfully!")
            return redirect("home")
        else:
            messages.error(request, "The account has not been created successfully")
    form = UserRegiserForm()
    categories = Category.objects.all().order_by("name").values()
    return render(request, 'signup.html', {
        "categories": categories,
        "form": form,
    })


def userlogout(request):
    logout(request)
    return redirect('loginauth')


def account(request):
    if not request.user.is_authenticated:
        messages.error(request, "Can't get access!")
    return render(request, 'account.html')
