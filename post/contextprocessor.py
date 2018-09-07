"""全局上下文"""
from post.models import *
from django.db.models import *
from datetime import date

def slider_context_processor(request):
    context = {}
    # 获取category列表
    context['category'] = Post.objects.values('category', 'category__name').annotate(count=Count('*'))
    # 按天归档
    archive = get_archive()
    context['archive'] = archive

    # 近期文章，以时间倒序分组
    context['recent'] = Post.objects.order_by('-created').all()[:5]
    return context

def get_archive():
    s = set()
    for t in Post.objects.values('created'):
        s.add(str(t['created'].year)+'-'+str(t['created'].month))
    archive = []
    for time in s:
        year = time.split('-')[0]
        month = time.split('-')[1]
        item = {'created':date(year=int(year),month=int(month),day=1),
                'count':Post.objects.filter(created__year=year,created__month=month).count}
        archive.append(item)
    return archive