from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("user/register", views.register_user, name="register_url"),
    path("user/login", views.login_user, name="login_url"),
    path("user/logout", views.logout_user, name="logout_url"),
    
    path("category/<str:category_name>", views.post_by_category, name = 'post_by_category'),
    path("single-post/<slug:slug>", views.single_post, name = 'single_post'),
    path("blogs/search", views.search, name= "search")
    
    
    # path("category/single-post/<slug:slug>", views.single_post, name = 'single_post'),
    # path("/blog_single", views.blog_single, name = 'blog_single'),
    # path("<slug:slug>", views.blog_single, name = 'blog_single'),
    # path("<int:category_id>", views.post_by_category, name = 'post_by_category'),
    # path("blog_single_alt/", views.blog_single_alt, name = 'blog_single_alt'),
    # path("pp/", views.personal, name = 'personal'),
]
