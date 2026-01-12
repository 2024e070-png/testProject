from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # 1. まずユーザーを作る
        self.user = User.objects.create_user(username='testuser', password='password')
        # 2. そのユーザーを使って Post オブジェクトを作る（これを self.post に保存）
        self.post = Post.objects.create(author=self.user, text='This is a test post')

    def test_post_str(self):
        # 3. テストメソッドの中で self.post を使う
        str_output = str(self.post)
        self.assertEqual(str_output, 'testuser: This is a test post')