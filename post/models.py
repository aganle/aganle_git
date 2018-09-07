from django.db import models
from django.core.paginator import Paginator   # 分页
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return u'%s' % self.name

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=20)
    desc = RichTextUploadingField()
    content = RichTextUploadingField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return u'%s' % self.title

    @staticmethod
    def get_posts_by_page(num, per_page=1):
        # num是通过url获得的当前页码，per_page是一页中显示的内容条数
        num = int(num)
        pagintor = Paginator(Post.objects.order_by('-modified').all(), per_page)
        if num < 1:
            num = 1
        elif num > pagintor.num_pages:
            num = pagintor.num_pages
        page = pagintor.page(num)

        previous = 2
        last = 2
        if num <= previous:
            start = 1
            end = last + previous + 1
        if num > previous:
            start = num - previous + 1
            end = num + last + 1
        if end > pagintor.num_pages:
            min = end - pagintor.num_pages
            end = pagintor.num_pages
            start -= min
            if start <= 1:
                start = 1
        return (page, range(start, end+1))
