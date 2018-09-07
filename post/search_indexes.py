from haystack import indexes
from post.models import *

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 给title设置索引
    title = indexes.CharField(model_attr='title')
    # 给内容设置索引
    content = indexes.CharField(model_attr='content')
    # 重写方法
    # 返回model类
    def get_model(self):
        return Post
    # 返回结果类
    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('created').all()
































