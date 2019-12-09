
参考：
https://paiza.hatenablog.com/entry/2018/02/28/paizacloud_django
https://qiita.com/tfrcm/items/27d2c9e4b3334447b6af

## 用語
リダイレクト : ページ遷移？

## プロジェクトの作成
1. django-admin startproject プロジェクト名
2. 動かすときはプロジェクトフォルダ内で　python3 manage.py runserver

## アプリケーションの作成
**アプリケーション**：プロジェクトの中に作成．機能ごとに作る
1. python3 manage.py startapp アプリケーション名

## ビューの追加
**ビュー**：アプリのロジックを書く．モデルに情報を要求し，それをテンプレートに渡す  
1. view.pyに記述   
2. myapp/urls.pyに紐づけ  
  ```python
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```
3. mypro/urls.pyにmyapp.urlsの記述を反映するよう追記（初回のみ？）  
  ```python
  urlpatterns = [
      path('myapp/', include('myapp.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

## モデルの追加
**モデル**：データを格納するテーブル  
1. models.pyに必要なフィールドと，そのデータの挙動を記載  
  ```python
  # Postという"post"テーブルに対応するモデルクラスを作成し、その中で"body"というテキストフィールドを作成
  class Post(models.Model):
      body = models.CharField(max_length=200)
  ```
2. settings.py→INSTALLED_APPS に追加してモデルを有効にする（アプリケーション名+Configになる）
    ```python
    # Application definition

    INSTALLED_APPS = [
        'myapp.apps.MyappConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    ```
3. python manage.py makemigrations myapp でマイグレーションスクリプトを作成  
    ※**マイグレーション**：Djangoがモデルの変更をディスク上のファイルに保存する方法  
    ※Djangoのモデルに変更があった事を伝え，その変更をマイグレーションの形で保存  
4. python manage.py migrate で未実行のマイグレーションスクリプトを実行  

## 管理サーバの利用
ブラウザ上でデータベースを管理する
1. python manage.py createsuperuser で管理用アカウント作成
2. myapp/admin.py にモデルを追加し，管理できるようにする
  ```python
  from .models import ModelName
  admin.site.register(ModelName)
  ```

## 静的ファイル（static:img,css,jsなど）
- myapp/static/myapp/ 以下に追加する
  ※ディレクトリを変更する場合は，settings.pyのSTATIC_URLをいじる
- htmlで呼び出すときには， {% load static %} を記述
  ```html
  {% load static %}
  <img src="{% static 'myapp/myimage.jpg' %}" />
  ```
