from django.urls import path
#from . import views
from .views import Home, ArticleDetailView, AddPostView
urlpatterns = [
    #path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('create_post/', AddPostView.as_view(), name='create_post'),

]
