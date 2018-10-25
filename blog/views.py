from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

# def post_list(request):
#     # 데이터베이스로부터 모든 Item내역을 가져올려고 한다.
#     qs = Post.objects.all()
#     return render(request, 'blog/post_list.html', {
#         'post_list': qs,
#     })
post_list = ListView.as_view(model=Post)