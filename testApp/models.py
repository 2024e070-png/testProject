# app/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    # 投稿者：Userモデルと紐づけ。ユーザーが消えたら投稿も消える設定
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 投稿内容：ここに <script> などを含めて実験します
    text = models.TextField()

    # 投稿日時
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 最初の20文字を管理画面などで表示
        return f'{self.author.username}: {self.text[:20]}'