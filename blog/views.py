from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# def post_list(request):
#     # 데이터베이스로부터 모든 Item내역을 가져올려고 한다.
#     qs = Post.objects.all()
#     return render(request, 'blog/post_list.html', {
#         'post_list': qs,
#     })
post_list = ListView.as_view(model=Post)


# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#   return render(request, 'blog/post_detail.html', {
#         'post': post,
#     })
post_detail = DetailView.as_view(model=Post)


# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save()
#             return redirect(f'/blog/{post.pk}')
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_form.html', {
#         'form': form,
#     })
post_new = CreateView.as_view(model=Post,
                              form_class=PostForm,
                              success_url='/blog/')

post_edit = UpdateView.as_view(model=Post,
                               form_class=PostForm,
                               success_url='/blog/')
post_delete = DeleteView.as_view(model=Post,
                                 success_url='/blog/')
