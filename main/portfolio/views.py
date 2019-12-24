from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Post
from .forms import PostForm

def index(request):
    # すべての情報をデータベースから取得
    posts = Post.objects.all()
    info = {
        'name': 'バシコ（小林菜穂子）',
        'age':22,
        'affiliation':'電気通信大学大学院 / 高橋（裕）lab',
        'research':'Machine learning, Image processing',
        'skills(勉強中)':'Matlab, R, Python, jupyter notebook',
        }

    title = "Naoko Kobayashi's portfolio"

    context = {'posts': posts,'info':info, 'title':title}
    # render()：テンプレートのロード，レンダリングのためのショートカット関数
    # 第1引数：request オブジェクト
    # 第2引数：テンプレート名
    # 第3引数（任意）：辞書
    return render(request, 'portfolio/index.html', context)


def edit(request):
    message = ""
    if request.method == 'POST':
        # 関数ベースviewの場合のみrequest.FILESが必要
        form = PostForm(request.POST, request.FILES)

        # データベースに保存
        if form.is_valid():
            form.save(commit=True)
            return redirect('portfolio:edit')
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
    return render(request, 'portfolio/edit.html', context)

def show_all_post(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'portfolio/show.html', context)



def update(request):

    from .forms import PostFormSet

    # GetのときはNoneとなり引数なしで呼び出したのと同じフォームが作られる
    formset = PostFormSet(request.POST or None)

    if request.method == 'POST' and formset.is_valid():
        formset = PostFormSet(request.POST,request.FILES)
        formset.save()
        return redirect('portfolio:update')

    context = {
        # 送信フォーム用空のPostFormオブジェクト
        'posts': Post.objects.all(),
        'formset': formset,
    }
    # reverse()：関数名からurlを逆引き．URLconfのパターンを指定
    #return HttpResponseRedirect(reverse('myapp:index'))
    # redirect()：HttpResponseRedirect+reverseのショートカット関数？
    return render(request, 'portfolio/update.html', context)
