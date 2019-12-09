from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    info ={'name': 'Bashiko', 'year':23 }
    # すべての情報をデータベースから取得
    posts = Post.objects.all()
    # 送信フォーム用空のPostFormオブジェクト
    form = PostForm()
    context = {'posts': posts, 'info':{'form': form,'name': 'Bashiko', 'year':23 }}
    # render()：テンプレートのロード，レンダリングのためのショートカット関数
    # 第1引数：request オブジェクト
    # 第2引数：テンプレート名
    # 第3引数（任意）：辞書
    return render(request, 'myapp/index.html', context)
