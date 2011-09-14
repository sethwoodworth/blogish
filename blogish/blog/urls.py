from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$',                              'list',      name='blog-list-newest'),
    url(r'^page/(\d+)/$',                   'list',      name='blog-list-page'),
    url(r'^0(\d+)/(.*)/$',                   'entry',     name='blog-entry'),
)
