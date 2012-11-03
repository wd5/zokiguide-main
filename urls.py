from django.conf.urls import patterns, include, url

# (?P<year>\d{4})
urlpatterns = patterns('',
    url(r'^$', 'main.views.home', name = 'home'),
)

