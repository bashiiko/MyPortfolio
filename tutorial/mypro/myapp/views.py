from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    # すべての情報をデータベースから取得
    posts = Post.objects.all()
    # 送信フォーム用空のPostFormオブジェクト
    form = PostForm()
    context = {'posts': posts, 'form': form}
    # render()：テンプレートのロード，レンダリングのためのショートカット関数
    # 第1引数：request オブジェクト
    # 第2引数：テンプレート名
    # 第3引数（任意）：辞書
    return render(request, 'myapp/index.html', context)

def create(request):
    form = PostForm(request.POST)
    # データベースに保存
    form.save(commit=True)
    # reverse()：関数名からurlを逆引き．URLconfのパターンを指定
    #return HttpResponseRedirect(reverse('myapp:index'))
    # redirect()：HttpResponseRedirect+reverseのショートカット関数？
    return redirect('myapp:index')

def delete(request, id=None):
    # get_object_or_404()：指定したIDに対応するデータがモデル内にない場合は，404を返す
    post = get_object_or_404(Post, pk=id)
    post.delete()
    #return HttpResponseRedirect(reverse('myapp:index'))
    return redirect('myapp:index')
