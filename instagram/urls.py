from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.login_page,name = 'come'),
    url('^home$',views.welcome,name = 'welcome'),
    url('^search/', views.search_results, name = 'search_results'),
    url(r'^new/article$', views.new_post, name='new-article'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/user/(\d+)$', views.view_users, name='users')

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
