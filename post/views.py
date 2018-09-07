from django.shortcuts import render
from haystack.query import SearchQuerySet
from post.models import *
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

# Create your views here.
def index_view(request, num='1'):
    page, page_range = Post.get_posts_by_page(num)
    return render(request, 'index.html', context={'page': page, 'page_range': page_range})

def post_detail_view(request, post_id):
    try:
        # 从数据库获取post类
        post = Post.objects.get(id=post_id)
    except:
        pass
    return render(request, 'details.html', {'post': post})

def category_details_view(request, category_id=None):
    posts = Post.objects.filter(category=category_id).order_by('-created')
    return render(request, 'archive.html', {'posts': posts})

def date_details_view(request, year,month):
    posts = Post.objects.filter(created__year=year, created__month=month).all()
    return render(request, 'archive.html', {'posts': posts})

def search_view(request):
    keyword = request.GET.get('q')
    from haystack.backends import SQ  # 类似django的Q
    paginator = Paginator(SearchQuerySet().filter(SQ(title=keyword) | SQ(content=keyword)).all(), 10)
    page = paginator.page(1)
    posts = []
    for result in page.object_list:
        posts.append(result.object)
    if posts:
        return render(request, 'archive.html', {'posts': posts})
    else:
        msg = '抱歉，未找到你所搜索的内容'
        return render(request, 'archive.html', {'msg': msg})