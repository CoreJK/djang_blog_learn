from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import ArticlePost

def article_list(request):
    # 取出所有博客文章
    articles = ArticlePost.objects.all()
    # 构造需要传递给模板的对象
    context = {'articles': articles}
    # 载入模板，返回渲染后的页面
    return render(request, 'article/list.html', context)

