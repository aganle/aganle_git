from django.conf.urls import url, static
from post import views

urlpatterns = [
    url(r'^$', views.index_view),
    url(r'^idnex.html/$', views.index_view),
    url(r'^page/(\d+)$', views.index_view),
    url(r'^post/details/(\d+)$', views.post_detail_view),
    url(r'^category/(\d+)$', views.category_details_view),
    url(r'^archive/(\d+)/(\d+)', views.date_details_view),
    url(r'^search/$', views.search_view)
]