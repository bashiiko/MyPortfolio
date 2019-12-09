from django.db import models

# Create your models here.
# Postという"post"テーブルに対応するモデルクラスを作成し、その中で"body"というテキストフィールドを作成
class Post(models.Model):
    body = models.CharField(max_length=200)
