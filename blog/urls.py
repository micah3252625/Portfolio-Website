from django.urls import path, include
from . import views
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', views.blog_thmb, name = 'blog_thmb'),
    path('blog-content|<slug:post>/', views.blog_detail, name = 'blog-content'),
    path('blog-category|<category>/', views.CatListView.as_view(), name = 'category'),
]
