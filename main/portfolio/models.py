from django.db import models,migrations
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='title', max_length=255)
    contents = models.TextField(verbose_name='contents', max_length=1000)
    image = models.ImageField(upload_to='upload/',verbose_name='image')
    tools = models.CharField(verbose_name='使用言語・ツール（複数ある場合はカンマで区切って入力）', max_length=255, blank=True, null=True)
    url = models.URLField(verbose_name='Url（任意）', max_length=255, blank=True, null=True)

    # admin画面などで、値を操作する際に必要になる
    # とりあえずどれか一個の値を返すようにしておく
    def __str__(self):
        return self.title

    def split_tools(self):
        return self.tools.split(',')

class PostActivity(models.Model):

    CHOICE = (
    ('', ' カテゴリーを選んでください '),
    ('0', '研究'),
    ('1', '学校生活'),
    ('2', 'その他'),
    )


    title = models.CharField(verbose_name='title', max_length=255)
    contents = models.TextField(verbose_name='contents（任意）', max_length=1000, blank=True, null=True)
    date = models.CharField(verbose_name='年月日など', max_length=255)
    category = models.CharField(verbose_name="category", choices=CHOICE, max_length=255)

    def __str__(self):
        return self.title


class User(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=255)
    password = models.CharField(verbose_name='password', max_length=10)
    #REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

class Login(models.Model):
    username = models.CharField(verbose_name='username', max_length=255)
    password = models.CharField(verbose_name='password', max_length=10)

    def __str__(self):
        return self.username
