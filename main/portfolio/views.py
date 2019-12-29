from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm
from .models import PostActivity
from .forms import PostActivityForm
from .models import Login
from .forms import LoginForm
from .models import User
from django.contrib.auth.models import User
from .forms import UserForm


def index(request):
    # すべての情報をデータベースから取得
    posts = Post.objects.all()
    posts_activity = PostActivity.objects.all()
    info = {
        'name': 'バシコ（小林菜穂子）',
        'age':22,
        'affiliation':'電気通信大学大学院 / 高橋（裕）lab',
        'research':'Machine learning, Image processing',
        'skills(勉強中)':'Matlab, R, Python, jupyter notebook',
        }

    urls = {
    'email':'bashiko.jobh[at]gmail.com',
    'github':'https://github.com/bashiiko',
    }

    title = "Naoko Kobayashi's portfolio"

    context = {'posts': posts, 'posts_activity' : posts_activity, 'info':info,
                'urls':urls, 'title':title}
    # render()：テンプレートのロード，レンダリングのためのショートカット関数
    # 第1引数：request オブジェクト
    # 第2引数：テンプレート名
    # 第3引数（任意）：辞書
    return render(request, 'portfolio/index.html', context)

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        # データベースに保存
        if form.is_valid():
            user = form.save()
            #username = form.cleaned_data.get('username')
            #password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=password)
            #user = User.objects.get(username=username,password=password )
            login(request, user)
            return redirect('portfolio:add_works')
    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'portfolio/create_user.html', context)

def Login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('portfolio:add_works')

    else:
        form = LoginForm()

    return render(request, 'portfolio/login.html' , {'form': form,})

def Logout(request):
    logout(request)
    return redirect('portfolio:index')

@login_required
def add_works(request):
    message = ""
    if request.method == 'POST':
        # 関数ベースviewの場合のみrequest.FILESが必要
        form = PostForm(request.POST, request.FILES)

        # データベースに保存
        if form.is_valid():
            form.save(commit=True)
            return redirect('portfolio:add_works')
        else:
            message = "アップロードに失敗しました"
    else:
        form = PostForm()

    context = {
        # 送信フォーム用空のPostFormオブジェクト
        'form': PostForm(),
        'message':message,
    }
    # reverse()：関数名からurlを逆引き．URLconfのパターンを指定
    #return HttpResponseRedirect(reverse('myapp:index'))
    # redirect()：HttpResponseRedirect+reverseのショートカット関数？
    return render(request, 'portfolio/add_works.html', context)

@login_required
def show_all_post_works(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'portfolio/show_works.html', context)

@login_required
def update_works(request):

    from .forms import PostFormSet

    # GetのときはNoneとなり引数なしで呼び出したのと同じフォームが作られる
    formset = PostFormSet(request.POST or None)

    if request.method == 'POST' and formset.is_valid():
        formset = PostFormSet(request.POST,request.FILES)
        formset.save()
        return redirect('portfolio:update_works')

    context = {
        # 送信フォーム用空のPostFormオブジェクト
        'posts': Post.objects.all(),
        'formset': formset,
    }
    # reverse()：関数名からurlを逆引き．URLconfのパターンを指定
    #return HttpResponseRedirect(reverse('myapp:index'))
    # redirect()：HttpResponseRedirect+reverseのショートカット関数？
    return render(request, 'portfolio/update_works.html', context)


@login_required
def add_activity(request):
    message = ""
    if request.method == 'POST':
        form = PostActivityForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=True)
            return redirect('portfolio:add_activity')
        else:
            message = "アップロードに失敗しました"
    else:
        form = PostActivityForm()

    context = {
        'form': PostActivityForm(),
        'message':message,
    }
    return render(request, 'portfolio/add_activity.html', context)

@login_required
def show_all_post_activity(request):
    context = {
        'posts': PostActivity.objects.all(),
    }
    return render(request, 'portfolio/show_activity.html', context)

@login_required
def update_activity(request):

    from .forms import PostActivityFormSet

    # GetのときはNoneとなり引数なしで呼び出したのと同じフォームが作られる
    formset = PostActivityFormSet(request.POST or None)

    if request.method == 'POST' and formset.is_valid():
        formset = PostActivityFormSet(request.POST,request.FILES)
        formset.save()
        return redirect('portfolio:update_activity')

    context = {
        # 送信フォーム用空のPostFormオブジェクト
        'posts': PostActivity.objects.all(),
        'formset': formset,
    }
    # reverse()：関数名からurlを逆引き．URLconfのパターンを指定
    #return HttpResponseRedirect(reverse('myapp:index'))
    # redirect()：HttpResponseRedirect+reverseのショートカット関数？
    return render(request, 'portfolio/update_activity.html', context)
